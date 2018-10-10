import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayBroadcast(unittest.TestCase):

    def test_plus(self):
        vector = np.arange(6).reshape(2, 3)
        assert_array_equal(vector, np.array([[0, 1, 2], [3, 4, 5]]))
        assert_array_equal(vector + 1, np.array([[1, 2, 3], [4, 5, 6]]))

    def test_multi(self):
        vector = np.arange(6).reshape(2, 3)
        assert_array_equal(vector, np.array([[0, 1, 2], [3, 4, 5]]))
        assert_array_equal(vector * 2, np.array([[0, 2, 4], [6, 8, 10]]))

if __name__ == '__main__':
    unittest.main()