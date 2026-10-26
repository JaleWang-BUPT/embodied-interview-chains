"""PyTorch interview examples: explicit shapes, masks, gradients and time axis.

Requires PyTorch. No pretrained weights or robot access.
"""

import math
import torch


def multihead_attention(x, w_qkv, w_out, heads, *, causal=False, valid=None):
    """x [B,T,D], weights [D,3D]/[D,D], valid [B,T] bool (True = data).

    Self-attention without biases, dropout or an attention library.
    Padding is masked both as keys and in the final query output.
    Fully masked rows return zeros rather than NaNs. Valid inputs and weights
    must be finite and their projections representable in the chosen dtype.
    """
    if x.ndim != 3:
        raise ValueError("x must have shape [B,T,D]")
    batch, length, dimension = x.shape
    if heads < 1 or dimension % heads or length == 0 or dimension == 0:
        raise ValueError("nonempty sequence, dimension divisible by heads required")
    if w_qkv.shape != (dimension, 3 * dimension):
        raise ValueError("w_qkv must be [D,3D]")
    if w_out.shape != (dimension, dimension):
        raise ValueError("w_out must be [D,D]")
    if valid is None:
        valid = torch.ones((batch, length), dtype=torch.bool, device=x.device)
    if valid.shape != (batch, length) or valid.dtype != torch.bool:
        raise ValueError("valid must be [B,T] bool")
    depth = dimension // heads
    # Remove invalid inputs before arithmetic: 0 * inf/NaN downstream is NaN.
    clean_x = x.masked_fill(~valid[:, :, None], 0.0)
    qkv = (clean_x @ w_qkv).reshape(batch, length, 3, heads, depth)
    q, k, v = qkv.permute(2, 0, 3, 1, 4).unbind(0)
    # Accumulate half/bfloat16 attention scores in float32.
    score_dtype = torch.float32 if x.dtype in (torch.float16, torch.bfloat16) else x.dtype
    scores = (q.to(score_dtype) @ k.to(score_dtype).transpose(-1, -2)) / math.sqrt(depth)
    allowed = valid[:, None, None, :].expand(batch, 1, length, length)
    if causal:
        triangle = torch.ones((length, length), dtype=torch.bool, device=x.device).tril()
        allowed = allowed & triangle
    scores = scores.masked_fill(~allowed, -torch.inf)
    scores = torch.where(allowed.any(dim=-1, keepdim=True), scores, 0.0)
    attention = torch.softmax(scores, dim=-1).masked_fill(~allowed, 0.0)
    context = attention.to(v.dtype) @ v
    result = context.transpose(1, 2).reshape(batch, length, dimension) @ w_out
    return result.masked_fill(~valid[:, :, None], 0.0)


def masked_velocity_mse(prediction, target, valid):
    """Mean over valid scalar entries; valid prediction/target must be finite.

    Padding may be nonfinite: it is removed before arithmetic and gradients.
    """
    if prediction.shape != target.shape or prediction.ndim != 3:
        raise ValueError("prediction/target must share [B,H,D]")
    if valid.shape != prediction.shape[:2] or valid.dtype != torch.bool:
        raise ValueError("valid must be [B,H] bool")
    # Mask BEFORE subtraction/squaring so NaN padding cannot poison gradients.
    clean_prediction = prediction.masked_fill(~valid[:, :, None], 0.0)
    clean_target = target.masked_fill(~valid[:, :, None], 0.0)
    masked = (clean_prediction - clean_target).square()
    denominator = (valid.sum() * prediction.shape[-1]).clamp(min=1)
    return masked.sum() / denominator


def flow_matching_loss(velocity, actions, condition, valid):
    """Straight path: x_t=(1-t)*noise+t*data; target velocity=data-noise.

    velocity(x_t, t[B], condition, valid[B,H]) must also mask padding inside
    any temporal attention. This function does not cross episode boundaries.
    """
    if actions.ndim != 3 or valid.shape != actions.shape[:2] or valid.dtype != torch.bool:
        raise ValueError("actions [B,H,D] and boolean valid [B,H] required")
    noise = torch.randn_like(actions)
    time = torch.rand(actions.shape[0], device=actions.device, dtype=actions.dtype)
    broadcast_time = time[:, None, None]
    mixed = (1 - broadcast_time) * noise + broadcast_time * actions
    mixed = mixed.masked_fill(~valid[:, :, None], 0.0)
    prediction = velocity(mixed, time, condition, valid)
    return masked_velocity_mse(prediction, actions - noise, valid)


@torch.no_grad()
def euler_sample(velocity, noise, condition, steps, valid=None):
    """Integrate from noise at t=0 to data at t=1, never t=1 back to noise."""
    if not isinstance(steps, int) or steps < 1 or noise.ndim != 3:
        raise ValueError("positive integer steps and [B,H,D] noise required")
    if valid is None:
        valid = torch.ones(noise.shape[:2], device=noise.device, dtype=torch.bool)
    if valid.shape != noise.shape[:2] or valid.dtype != torch.bool:
        raise ValueError("valid must be [B,H] bool")
    state = noise.clone().masked_fill(~valid[:, :, None], 0.0)
    for index in range(steps):
        time = torch.full(
            (noise.shape[0],), index / steps, device=noise.device, dtype=noise.dtype
        )
        state = state + velocity(state, time, condition, valid) / steps
        state = state.masked_fill(~valid[:, :, None], 0.0)
    return state


def ppo_actor_loss(new_log_probability, old_log_probability, advantage, epsilon=0.2):
    """Already-reduced per-action log-probability [N], detached old policy/GAE.

    This is only the actor term, not a complete PPO training implementation.
    The caller must normalize/validate advantages and manage the rollout policy.
    Inputs must be finite, with log-ratio safely exponentiable in their dtype;
    monitor abnormal ratios rather than silently clipping the log-ratio.
    """
    if (
        new_log_probability.ndim != 1
        or old_log_probability.shape != new_log_probability.shape
        or advantage.shape != new_log_probability.shape
        or new_log_probability.numel() == 0
        or not 0 < epsilon < 1
    ):
        raise ValueError("matching nonempty [N] inputs and epsilon in (0,1) required")
    ratio = (new_log_probability - old_log_probability.detach()).exp()
    advantage = advantage.detach()
    direct = ratio * advantage
    clipped = ratio.clamp(1 - epsilon, 1 + epsilon) * advantage
    return -torch.minimum(direct, clipped).mean()
