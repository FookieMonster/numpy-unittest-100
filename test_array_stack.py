import unittest
import numpy as np
from numpy.testing import assert_array_equal

# スタック
class TestArrayStack(unittest.TestCase):

    # vstack関数
    def test_vstack(self):
        metrixA = np.array([[1, 2], [3, 4]])
        metrixB = np.array([[5, 6], [7, 8]])
        metrixC = np.vstack((metrixA, metrixB))
        assert_array_equal(metrixC,
                          np.array([[x, x],
                                    [x, x],
                                    [x, x],
                                    [x, x]]))

    # hstack関数
    def test_hstack(self):
        metrixA = np.array([[1, 2], [3, 4]])
        metrixB = np.array([[5, 6], [7, 8]])
        metrixC = np.hstack((metrixA, metrixB))
        assert_array_equal(metrixC,
                          np.array([[x, x, x, x],
                                    [x, x, x, x]]))

if __name__ == '__main__':
    unittest.main()
