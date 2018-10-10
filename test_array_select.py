import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArraySelect(unittest.TestCase):

    def test_select_cond1(self):
        vector = np.arange(10)
        vector = np.select([5 < vector], [vector ** 2])
        assert_array_equal(vector, np.array([0, 0, 0, 0, 0, 0, 36, 49, 64, 81]))

    def test_select_cond2(self):
        vector = np.arange(10)
        vector = np.select([vector < 3, 5 < vector], [vector, vector ** 2])
        assert_array_equal(vector, np.array([0, 1, 2, 0, 0, 0, 36, 49, 64, 81]))

if __name__ == '__main__':
    unittest.main()