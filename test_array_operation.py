import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayOperation(unittest.TestCase):

    def test_plus(self):
        vector = np.array([0, 0, 0, 0, 0])
        vector = vector + 1
        assert_array_equal(vector, np.array([1, 1, 1, 1, 1]))

    def test_minus(self):
        vector = np.array([1, 1, 1, 1, 1])
        vector = vector - 1
        assert_array_equal(vector, np.array([0, 0, 0, 0, 0]))

    def test_multi(self):
        vector = np.array([3, 3, 3, 3, 3])
        vector = vector * 3
        assert_array_equal(vector, np.array([9, 9, 9, 9, 9]))

    def test_dot(self):
        vector = np.array([[1, 2], [3, 4]])
        vector = np.dot(vector, vector)
        assert_array_equal(vector, np.array([[7, 10], [15, 22]]))

    def test_expo(self):
        vector = np.array([3, 3, 3, 3, 3])
        vector = vector ** 2
        assert_array_equal(vector, np.array([9, 9, 9, 9, 9]))

    def test_bool(self):
        vector = np.array([0, 1, 2, 3, 4])
        vector = vector < 3
        assert_array_equal(vector, np.array([True, True, True, False, False]))

    def test_sum(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        self.assertEqual(metrix.sum(), 45)

    def test_max(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        self.assertEqual(metrix.max(), 9)

    def test_min(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        self.assertEqual(metrix.min(), 0)

    def test_sum_axis0(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.sum(axis=0), np.array([5, 7, 9, 11, 13]))

    def test_sum_axis1(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.sum(axis=1), np.array([10, 35]))

    def test_max_axis0(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.max(axis=0), np.array([5, 6, 7, 8, 9]))

    def test_max_axis1(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.max(axis=1), np.array([4, 9]))

    def test_min_axis0(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.min(axis=0), np.array([0, 1, 2, 3, 4]))

    def test_min_axis1(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(metrix.min(axis=1), np.array([0, 5]))

    def test_transpose(self):
        metrix = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        assert_array_equal(metrix.transpose(), np.array([[0, 3, 6], [1, 4, 7], [2, 5, 8]]))

    def test_T(self):
        metrix = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        assert_array_equal(metrix.T, np.array([[0, 3, 6], [1, 4, 7], [2, 5, 8]]))

    def test_flatten(self):
        metrix = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        assert_array_equal(metrix.flatten(), np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]))

if __name__ == '__main__':
    unittest.main()