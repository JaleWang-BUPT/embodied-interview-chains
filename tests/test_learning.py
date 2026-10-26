import importlib.util
import unittest

HAS_TORCH = importlib.util.find_spec("torch") is not None
if HAS_TORCH:
    import torch
    import torch.nn.functional as F
    from examples.learning import (
        euler_sample, flow_matching_loss, masked_velocity_mse,
        multihead_attention, ppo_actor_loss,
    )


@unittest.skipUnless(HAS_TORCH, "PyTorch optional dependency is not installed")
class LearningTests(unittest.TestCase):
    def setUp(self):
        torch.manual_seed(7)

    def test_attention_matches_pytorch_reference(self):
        x = torch.randn(2, 4, 8, dtype=torch.float64)
        qkv, output = torch.randn(8, 24, dtype=x.dtype), torch.randn(8, 8, dtype=x.dtype)
        got = multihead_attention(x, qkv, output, 2, causal=True)
        q, k, v = (x @ qkv).reshape(2, 4, 3, 2, 4).permute(2, 0, 3, 1, 4)
        reference = F.scaled_dot_product_attention(q, k, v, is_causal=True)
        reference = reference.transpose(1, 2).reshape(2, 4, 8) @ output
        torch.testing.assert_close(got, reference)

    def test_causal_attention_cannot_see_future_and_gradients_are_finite(self):
        x = torch.randn(1, 4, 8, requires_grad=True)
        qkv, output = torch.randn(8, 24), torch.randn(8, 8)
        original = multihead_attention(x, qkv, output, 2, causal=True)
        changed = x.detach().clone()
        changed[:, -1] += 100
        later = multihead_attention(changed, qkv, output, 2, causal=True)
        torch.testing.assert_close(original[:, :-1], later[:, :-1])
        original.square().mean().backward()
        self.assertTrue(torch.isfinite(x.grad).all())

    def test_padding_and_fully_masked_batch_are_zero(self):
        x = torch.randn(2, 3, 4, requires_grad=True)
        valid = torch.tensor([[False, False, False], [True, True, False]])
        qkv, output = torch.randn(4, 12), torch.randn(4, 4)
        got = multihead_attention(x, qkv, output, 2, causal=True, valid=valid)
        self.assertTrue(torch.isfinite(got).all())
        self.assertEqual(got[~valid].abs().sum().item(), 0)
        changed = x.clone()
        changed[~valid] = 1000
        torch.testing.assert_close(
            got, multihead_attention(changed, qkv, output, 2, causal=True, valid=valid)
        )
        got.square().sum().backward()
        self.assertTrue(torch.isfinite(x.grad).all())
        self.assertEqual(x.grad[~valid].abs().sum().item(), 0)

    def test_padding_matches_sdpa_reference(self):
        x = torch.randn(2, 4, 8, dtype=torch.float64)
        valid = torch.tensor([[True, True, False, False], [True, True, True, False]])
        qkv, output = torch.randn(8, 24, dtype=x.dtype), torch.randn(8, 8, dtype=x.dtype)
        got = multihead_attention(x, qkv, output, 2, causal=True, valid=valid)
        clean = x.masked_fill(~valid[:, :, None], 0)
        q, k, v = (clean @ qkv).reshape(2, 4, 3, 2, 4).permute(2, 0, 3, 1, 4)
        allowed = valid[:, None, None, :] & torch.ones(4, 4, dtype=torch.bool).tril()
        expected = F.scaled_dot_product_attention(q, k, v, attn_mask=allowed)
        expected = expected.transpose(1, 2).reshape(2, 4, 8) @ output
        expected = expected.masked_fill(~valid[:, :, None], 0)
        torch.testing.assert_close(got, expected)

    def test_attention_rejects_invalid_shapes(self):
        with self.assertRaises(ValueError):
            multihead_attention(torch.zeros(1, 3, 5), torch.zeros(5, 15), torch.eye(5), 2)

    def test_half_precision_padding_is_removed_before_projection(self):
        x = torch.tensor([[[1., 1.], [60000., 60000.]]], dtype=torch.float16)
        valid = torch.tensor([[True, False]])
        got = multihead_attention(
            x, torch.ones(2, 6, dtype=x.dtype), torch.eye(2, dtype=x.dtype),
            1, valid=valid,
        )
        self.assertTrue(torch.isfinite(got).all())
        torch.testing.assert_close(got, torch.tensor([[[2., 2.], [0., 0.]]], dtype=x.dtype))

    def test_nan_padding_does_not_poison_loss_or_gradients(self):
        prediction = torch.tensor([[[2., 4.], [float("nan"), float("nan")]]], requires_grad=True)
        target = torch.tensor([[[0., 0.], [float("nan"), float("nan")]]], requires_grad=True)
        loss = masked_velocity_mse(prediction, target, torch.tensor([[True, False]]))
        self.assertEqual(loss.item(), 10)
        loss.backward()
        torch.testing.assert_close(prediction.grad, torch.tensor([[[2., 4.], [0., 0.]]]))
        torch.testing.assert_close(target.grad, torch.tensor([[[-2., -4.], [0., 0.]]]))

    def test_padding_loss_and_gradient(self):
        prediction = torch.tensor([[[2., 4.], [100., 100.]]], requires_grad=True)
        target = torch.zeros_like(prediction)
        valid = torch.tensor([[True, False]])
        loss = masked_velocity_mse(prediction, target, valid)
        self.assertEqual(loss.item(), 10)
        loss.backward()
        torch.testing.assert_close(prediction.grad, torch.tensor([[[2., 4.], [0., 0.]]]))
        empty_loss = masked_velocity_mse(prediction, target, torch.zeros_like(valid))
        self.assertEqual(empty_loss.item(), 0)

    def test_flow_path_and_mask_contract(self):
        actions = torch.randn(2, 3, 4)
        valid = torch.tensor([[True, True, False], [True, False, False]])
        condition = object()

        def exact_velocity(mixed, time, supplied_condition, supplied_valid):
            self.assertIs(supplied_condition, condition)
            self.assertIs(supplied_valid, valid)
            self.assertEqual(mixed[~valid].abs().sum().item(), 0)
            noise = (mixed - time[:, None, None] * actions) / (1 - time[:, None, None])
            return actions - noise

        self.assertLess(flow_matching_loss(exact_velocity, actions, condition, valid).item(), 1e-8)

    def test_euler_constant_field_and_padding(self):
        initial = torch.zeros(2, 3, 4)
        valid = torch.tensor([[True, True, False], [True, False, False]])
        result = euler_sample(
            lambda state, time, condition, mask: torch.ones_like(state) * 2,
            initial, None, 10, valid,
        )
        torch.testing.assert_close(result[valid], torch.full_like(result[valid], 2))
        self.assertEqual(result[~valid].abs().sum().item(), 0)
        self.assertFalse(result.requires_grad)
        with self.assertRaises(ValueError):
            euler_sample(None, initial, None, 0)

    def test_ppo_sign_clipping_and_detach(self):
        log_new = torch.tensor([2., -2.], requires_grad=True)
        log_old = torch.zeros(2, requires_grad=True)
        advantage = torch.tensor([1., -1.], requires_grad=True)
        loss = ppo_actor_loss(log_new, log_old, advantage)
        self.assertAlmostEqual(loss.item(), -0.2, places=6)
        loss.backward()
        torch.testing.assert_close(log_new.grad, torch.zeros(2))
        self.assertIsNone(log_old.grad)
        self.assertIsNone(advantage.grad)

    def test_ppo_unclipped_gradient(self):
        log_new = torch.zeros(2, requires_grad=True)
        loss = ppo_actor_loss(log_new, torch.zeros(2), torch.tensor([1., -1.]))
        loss.backward()
        torch.testing.assert_close(log_new.grad, torch.tensor([-0.5, 0.5]))


if __name__ == "__main__":
    unittest.main()
