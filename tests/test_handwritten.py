import math
import unittest

from examples.handwritten import (
    PID, ListNode, conv2d_valid, kalman_scalar, kth_largest,
    newton_root, reverse_list, rotate_z, shortest_path, stable_softmax,
)


class HandwrittenTests(unittest.TestCase):
    def test_softmax_extreme_and_translation_invariance(self):
        expected = stable_softmax([0, 1, 2])
        for got, want in zip(stable_softmax([10000, 10001, 10002]), expected):
            self.assertAlmostEqual(got, want)
        self.assertEqual(stable_softmax([10000, 0], temperature=1e-10), [1.0, 0.0])
        self.assertAlmostEqual(sum(expected), 1)

    def test_softmax_rejects_undefined_inputs(self):
        for data, temp in [([], 1), ([1], 0), ([math.inf], 1), ([math.nan], 1)]:
            with self.assertRaises(ValueError):
                stable_softmax(data, temp)

    def test_softmax_extreme_difference_with_large_temperature(self):
        got = stable_softmax([-1e308, 1e308], temperature=1e308)
        self.assertAlmostEqual(got[0], 1 / (1 + math.exp(2)))
        self.assertAlmostEqual(got[1], 1 / (1 + math.exp(-2)))

    def test_conv_non_square_and_identity(self):
        self.assertEqual(
            conv2d_valid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 0], [0, -1]]),
            [[-4.0, -4.0], [-4.0, -4.0]],
        )
        self.assertEqual(conv2d_valid([[2, 4, 6]], [[1]]), [[2.0, 4.0, 6.0]])
        with self.assertRaises(ValueError):
            conv2d_valid([[1], [2, 3]], [[1]])

    def test_pid_saturation_does_not_wind_up(self):
        controller = PID(kp=1, ki=1, lower=-1, upper=1)
        for _ in range(100):
            self.assertEqual(controller.step(10, 0, 0.1), 1)
        self.assertEqual(controller.integral, 0)
        self.assertEqual(controller.step(0, 0, 0.1), 0)
        with self.assertRaises(ValueError):
            controller.step(1, 0, 0)

    def test_pid_integral_can_unwind_and_pd_has_no_integral_growth(self):
        controller = PID(kp=0, ki=1, integral=2, lower=-1, upper=1)
        controller.step(-1, 0, 0.1)
        self.assertLess(controller.integral, 2)
        pd = PID(kp=1, kd=0.2)
        pd.step(1, 0, 0.1)
        self.assertEqual(pd.integral, 0)

    def test_rotation_preserves_norm_and_has_inverse(self):
        for got, want in zip(rotate_z((1., 0., 0.), math.pi / 2), (0., 1., 0.)):
            self.assertAlmostEqual(got, want)
        original = (1.0, 2.0, 3.0)
        turned = rotate_z(original, math.pi / 3)
        self.assertAlmostEqual(sum(x*x for x in original), sum(x*x for x in turned))
        for got, want in zip(rotate_z(turned, -math.pi / 3), original):
            self.assertAlmostEqual(got, want)

    def test_newton_success_and_failures(self):
        root = newton_root(lambda x: x*x-2, lambda x: 2*x, 1)
        self.assertAlmostEqual(root, math.sqrt(2))
        with self.assertRaises(ValueError):
            newton_root(lambda x: x*x-2, lambda x: 2*x, 0)
        with self.assertRaises(RuntimeError):
            newton_root(lambda x: x*x-2, lambda x: 2*x, 10, max_steps=1)

    def test_newton_rejects_invalid_parameters_and_final_nonfinite_residual(self):
        for options in ({"tolerance": math.inf}, {"tolerance": math.nan},
                        {"max_steps": 1.5}, {"max_steps": True}):
            with self.assertRaises(ValueError):
                newton_root(lambda x: x, lambda x: 1, 1, **options)
        with self.assertRaises(ValueError):
            newton_root(lambda x: 1 if x == 0 else math.nan, lambda x: 1, 0, max_steps=1)

    def test_kalman_gain_moves_with_q_and_r(self):
        low_r = kalman_scalar(0, 1, 10, 0.1, 0.1)
        high_r = kalman_scalar(0, 1, 10, 0.1, 10)
        high_q = kalman_scalar(0, 1, 10, 10, 10)
        self.assertGreater(low_r[2], high_r[2])
        self.assertGreater(high_q[2], high_r[2])
        self.assertGreaterEqual(low_r[1], 0)
        self.assertAlmostEqual(low_r[1], (1-low_r[2])*1.1)
        with self.assertRaises(ValueError):
            kalman_scalar(0, 1, 0, 0, 0)

    def test_list_reverse_empty_single_and_identity(self):
        self.assertIsNone(reverse_list(None))
        single = ListNode(7)
        self.assertIs(reverse_list(single), single)
        self.assertIsNone(single.next)
        nodes = [ListNode(i) for i in range(3)]
        nodes[0].next, nodes[1].next = nodes[1], nodes[2]
        result = reverse_list(nodes[0])
        self.assertIs(result, nodes[2])
        self.assertIs(result.next, nodes[1])
        self.assertIs(result.next.next, nodes[0])
        self.assertIsNone(nodes[0].next)

    def test_heap_duplicates_and_bounds(self):
        self.assertEqual(kth_largest([3, 1, 3, -1], 2), 3)
        self.assertEqual(kth_largest(iter([3, 1, -1]), 3), -1)
        with self.assertRaises(ValueError):
            kth_largest([1], 2)
        for k in (0, -1, 1.5, True):
            with self.assertRaises(ValueError):
                kth_largest([3, 2, 1], k)

    def test_bfs_cycle_disconnected_and_start_is_goal(self):
        graph = {"a": ["b", "c"], "b": ["a", "d"], "c": ["d"]}
        self.assertEqual(shortest_path(graph, "a", "d"), ["a", "b", "d"])
        self.assertIsNone(shortest_path(graph, "a", "z"))
        self.assertEqual(shortest_path(graph, "a", "a"), ["a"])


if __name__ == "__main__":
    unittest.main()
