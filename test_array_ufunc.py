import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayUfunc(unittest.TestCase):

    def test_sqrt(self):
        vector = np.array([9, 16, 25])
        assert_array_equal(np.sqrt(vector), np.array([x, x, x]))

    def test_add(self):
        A = np.array([0, 1, 2])
        B = np.array([2, -1, 4])
        assert_array_equal(np.add(A, B), np.array([x, x, x]))

if __name__ == '__main__':
    unittest.main()