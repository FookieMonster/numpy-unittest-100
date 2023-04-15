import unittest
import numpy as np
from numpy.testing import assert_array_equal

# ブロードキャスト
class TestArrayBroadcast(unittest.TestCase):

    # 足し算のブロードキャスト
    def test_plus(self):
        vector = np.arange(6).reshape(2, 3)
        assert_array_equal(vector, np.array([[0, 1, 2], [3, 4, 5]]))
        assert_array_equal(vector + 1, np.array([[x, x, x], [x, x, x]]))

    # 引き算のブロードキャスト
    def test_minus(self):
        vector = np.arange(6).reshape(2, 3)
        assert_array_equal(vector, np.array([[0, 1, 2], [3, 4, 5]]))
        assert_array_equal(vector - 1, np.array([[x, x, x], [x, x, x]]))

    # 掛け算のブロードキャスト
    def test_multi(self):
        vector = np.arange(6).reshape(2, 3)
        assert_array_equal(vector, np.array([[0, 1, 2], [3, 4, 5]]))
        assert_array_equal(vector * 2, np.array([[x, x, x], [x, x, x]]))

    # べき乗のブロードキャスト
    def test_square(self):
        vector = np.arange(6).reshape(2, 3)
        assert_array_equal(vector, np.array([[0, 1, 2], [3, 4, 5]]))
        assert_array_equal(vector ** 2, np.array([[x, x, x], [x, x, x]]))

if __name__ == '__main__':
    unittest.main()
