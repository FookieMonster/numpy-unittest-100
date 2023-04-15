import unittest
import numpy as np
from numpy.testing import assert_array_equal

# 基本的な操作
class TestArrayOperation(unittest.TestCase):

    def test_plus(self):
        vector = np.array([0, 0, 0, 0, 0])
        vector = vector + 1
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_minus(self):
        vector = np.array([1, 1, 1, 1, 1])
        vector = vector - 1
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_multi(self):
        vector = np.array([3, 3, 3, 3, 3])
        vector = vector * 3
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_dot(self):
        vector = np.array([[1, 2], [3, 4]])
        vector = np.dot(vector, vector)
        assert_array_equal(vector, np.array([[x, x], [x, x]]))

    def test_expo(self):
        vector = np.array([3, 3, 3, 3, 3])
        vector = vector ** 2
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_bool(self):
        vector = np.array([0, 1, 2, 3, 4])
        vector = vector < 3
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_sum(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        self.assertEqual(metrix.sum(), x)

    def test_max(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        self.assertEqual(metrix.max(), x)

    def test_min(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        self.assertEqual(metrix.min(), x)

    def test_sum_axis0(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.sum(axis=0), np.array([x, x, x, x, x]))

    def test_sum_axis1(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.sum(axis=1), np.array([x, x]))

    def test_max_axis0(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.max(axis=0), np.array([x, x, x, x, x]))

    def test_max_axis1(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.max(axis=1), np.array([x, x]))

    def test_min_axis0(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.min(axis=0), np.array([x, x, x, x, x]))

    def test_min_axis1(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.min(axis=1), np.array([x, x]))

    def test_transpose(self):
        metrix = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        assert_array_equal(metrix.transpose(), np.array([[x, x, x], [x, x, x], [x, x, x]]))

    def test_T(self):
        metrix = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        assert_array_equal(metrix.T, np.array([[x, x, x], [x, x, x], [x, x, x]]))

    def test_flatten(self):
        metrix = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        assert_array_equal(metrix.flatten(), np.array([x, x, x, x, x, x, x, x, x]))

if __name__ == '__main__':
    unittest.main()
