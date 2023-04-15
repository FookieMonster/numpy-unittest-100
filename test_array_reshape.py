import unittest
import numpy as np
from numpy.testing import assert_array_equal

# 形状の操作
class TestArrayReshape(unittest.TestCase):

    def test_reshape2d(self):
        metrix = np.arange(6).reshape(2, 3)
        assert_array_equal(metrix, np.array([[x, x, x], [x, x, x]]))

    def test_reshape3d(self):
        metrix = np.arange(24).reshape(2, 3, 4)
        np.set_printoptions(threshold=np.inf)
        assert_array_equal(metrix, np.array([[[x, x, x, x], [x, x, x, x], [x, x, x, x]],
                                            [[x, x, x, x], [x, x, x, x], [x, x, x, x]]]))

    def test_reshape_auto(self):
        metrix = np.arange(6).reshape(2, -1)
        assert_array_equal(metrix, np.array([[x, x, x], [x, x, x]]))

    def test_flatten(self):
        metrix = np.array([[12,  6, 18],
                           [ 2, 14, 14],
                           [10, 19,  0]])
        assert_array_equal(metrix.flatten(), np.array([x, x, x, x, x, x, x, x, x]))

if __name__ == '__main__':
    unittest.main()
