import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayStats(unittest.TestCase):

    def test_sum(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        self.assertEqual(np.sum(metrix), 45)

    def test_max(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        self.assertEqual(np.max(metrix), 9)

    def test_min(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        self.assertEqual(np.min(metrix), 0)

    def test_sum_axis0(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(np.sum(metrix, axis=0), np.array([5, 7, 9, 11, 13]))

    def test_sum_axis1(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(np.sum(metrix, axis=1), np.array([10, 35]))

    def test_max_axis0(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(np.max(metrix, axis=0), np.array([5, 6, 7, 8, 9]))

    def test_max_axis1(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(np.max(metrix, axis=1), np.array([4, 9]))

    def test_min_axis0(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(np.min(metrix, axis=0), np.array([0, 1, 2, 3, 4]))

    def test_min_axis1(self):
        metrix = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        assert_array_equal(np.min(metrix, axis=1), np.array([0, 5]))

if __name__ == '__main__':
    unittest.main()