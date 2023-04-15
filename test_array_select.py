import unittest
import numpy as np
from numpy.testing import assert_array_equal

# 配列の選択
class TestArraySelect(unittest.TestCase):

    def test_select_cond1(self):
        vector = np.arange(10)
        vector = np.select([5 < vector], [vector ** 2])
        assert_array_equal(vector, np.array([x, x, x, x, x, x, x, x, x, x]))

    def test_select_cond2(self):
        vector = np.arange(10)
        vector = np.select([vector < 3, 5 < vector], [vector, vector ** 2])
        assert_array_equal(vector, np.array([x, x, x, x, x, x, x, x, x, x]))

if __name__ == '__main__':
    unittest.main()
