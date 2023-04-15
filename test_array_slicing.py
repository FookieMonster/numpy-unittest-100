import unittest
import numpy as np
from numpy.testing import assert_array_equal

# スライス
class TestArraySlicing(unittest.TestCase):

    def test_slicing_1d(self):
        vector = np.arange(10)
        assert_array_equal(vector[2:5], np.array([x, x, x]))

    def test_slicing_1d_with_step(self):
        vector = np.arange(10)
        assert_array_equal(vector[0:10:2], np.array([x, x, x, x, x]))

    def test_slicing_1d_reverse(self):
        vector = np.arange(10)
        assert_array_equal(vector[::-1], np.array([x, x, x, x, x, x, x, x, x, x]))

    def test_slicing_2d(self):
        metrix = np.arange(9).reshape(3, 3)
        assert_array_equal(metrix[0:2, 0:2], np.array([[x, x], [x, x]]))

if __name__ == '__main__':
    unittest.main()
