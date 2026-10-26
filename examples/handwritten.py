"""Small, readable interview implementations; not robot production controllers."""

from collections import deque
from dataclasses import dataclass
import heapq
import math


def stable_softmax(values, temperature=1.0):
    """Finite, nonempty input; temperature must be positive and finite."""
    values = list(values)
    if not values or not math.isfinite(temperature) or temperature <= 0:
        raise ValueError("nonempty values and positive finite temperature required")
    if not all(math.isfinite(x) for x in values):
        raise ValueError("values must be finite")
    # Usually subtract first. Opposite-sign extreme values can overflow that
    # subtraction; in that case scaling first also handles very large T.
    maximum = max(values)
    weights = []
    for value in values:
        difference = value - maximum
        scaled = (
            difference / temperature if math.isfinite(difference)
            else value / temperature - maximum / temperature
        )
        weights.append(math.exp(scaled))
    total = math.fsum(weights)
    return [x / total for x in weights]


def conv2d_valid(image, kernel):
    """One channel, stride 1, valid cross-correlation (DL conv convention)."""
    height, kh = len(image), len(kernel)
    if height == 0 or kh == 0:
        raise ValueError("empty image or kernel")
    width, kw = len(image[0]), len(kernel[0])
    if not width or not kw or kh > height or kw > width:
        raise ValueError("invalid dimensions")
    if any(len(row) != width for row in image):
        raise ValueError("ragged image")
    if any(len(row) != kw for row in kernel):
        raise ValueError("ragged kernel")
    return [
        [
            math.fsum(
                image[y + ky][x + kx] * kernel[ky][kx]
                for ky in range(kh)
                for kx in range(kw)
            )
            for x in range(width - kw + 1)
        ]
        for y in range(height - kh + 1)
    ]


@dataclass
class PID:
    """Scalar PID, conditional integration; error derivative may kick on steps."""

    kp: float
    ki: float = 0.0
    kd: float = 0.0
    lower: float = -1.0
    upper: float = 1.0
    integral: float = 0.0
    previous_error: float | None = None

    def __post_init__(self):
        if self.lower >= self.upper or not all(
            math.isfinite(x)
            for x in (self.kp, self.ki, self.kd, self.lower, self.upper)
        ):
            raise ValueError("finite gains and ordered finite output limits required")
        if self.ki < 0:
            raise ValueError("this conditional-integration example assumes ki >= 0")

    def step(self, target, measurement, dt):
        if dt <= 0 or not all(math.isfinite(x) for x in (target, measurement, dt)):
            raise ValueError("finite inputs and positive dt required")
        error = target - measurement
        derivative = 0.0 if self.previous_error is None else (
            error - self.previous_error
        ) / dt
        candidate = self.integral + error * dt if self.ki else self.integral
        raw = self.kp * error + self.ki * candidate + self.kd * derivative
        output = min(self.upper, max(self.lower, raw))
        if (
            raw == output
            or (raw > self.upper and error < 0)
            or (raw < self.lower and error > 0)
        ):
            self.integral = candidate
        self.previous_error = error
        return output


def rotate_z(vector, angle):
    """Active right-handed Z rotation, radians, column-vector convention."""
    if len(vector) != 3:
        raise ValueError("3D vector required")
    x, y, z = vector
    c, s = math.cos(angle), math.sin(angle)
    return (c * x - s * y, s * x + c * y, z)


def newton_root(function, derivative, initial, tolerance=1e-10, max_steps=50):
    """Residual-based stopping; raises instead of silently returning failure."""
    if (
        not math.isfinite(tolerance) or tolerance <= 0
        or type(max_steps) is not int or max_steps < 1
        or not math.isfinite(initial)
    ):
        raise ValueError("invalid solver parameters")
    value = initial
    for _ in range(max_steps):
        residual = function(value)
        if not math.isfinite(residual):
            raise ValueError("nonfinite residual")
        if abs(residual) <= tolerance:
            return value
        slope = derivative(value)
        if not math.isfinite(slope) or abs(slope) < 1e-14:
            raise ValueError("derivative too small or nonfinite")
        value -= residual / slope
        if not math.isfinite(value):
            raise ValueError("nonfinite iterate")
    residual = function(value)
    if not math.isfinite(residual):
        raise ValueError("nonfinite residual")
    if abs(residual) <= tolerance:
        return value
    raise RuntimeError("Newton iteration did not converge")


def kalman_scalar(mean, variance, measurement, process_variance, sensor_variance):
    """1D random-walk state, identity observation; Q/R are variances."""
    numbers = (mean, variance, measurement, process_variance, sensor_variance)
    if not all(math.isfinite(x) for x in numbers):
        raise ValueError("finite parameters required")
    if variance < 0 or process_variance < 0 or sensor_variance <= 0:
        raise ValueError("P,Q must be nonnegative and R positive")
    predicted_variance = variance + process_variance
    gain = predicted_variance / (predicted_variance + sensor_variance)
    updated_mean = mean + gain * (measurement - mean)
    # Joseph covariance form in this scalar model.
    updated_variance = (
        (1 - gain) ** 2 * predicted_variance + gain**2 * sensor_variance
    )
    return updated_mean, updated_variance, gain


@dataclass
class ListNode:
    value: object
    next: "ListNode | None" = None


def reverse_list(head):
    """Assumes an acyclic list. O(n) time, O(1) additional memory."""
    previous = None
    while head is not None:
        following = head.next
        head.next = previous
        previous, head = head, following
    return previous


def kth_largest(values, k):
    """Bounded min-heap; duplicate values count separately."""
    if type(k) is not int or k < 1:
        raise ValueError("k must be a positive integer (not bool)")
    heap = []
    for value in values:
        if len(heap) < k:
            heapq.heappush(heap, value)
        elif value > heap[0]:
            heapq.heapreplace(heap, value)
    if len(heap) < k:
        raise ValueError("k exceeds input length")
    return heap[0]


def shortest_path(graph, start, goal):
    """Directed, unweighted graph. Returns one path, or None if unreachable."""
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        if node == goal:
            path = [node]
            while path[-1] != start:
                path.append(parent[path[-1]])
            return list(reversed(path))
        for neighbour in graph.get(node, ()):
            if neighbour not in parent:
                parent[neighbour] = node
                queue.append(neighbour)
    return None
