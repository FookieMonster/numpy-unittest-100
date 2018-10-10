import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayReshape(unittest.TestCase):

    def test_reshape2d(self):
        metrix = np.arange(6).reshape(2, 3)
        assert_array_equal(metrix, np.array([[0, 1, 2], [3, 4, 5]]))

    def test_reshape3d(self):
        metrix = np.arange(24).reshape(2, 3, 4)
        np.set_printoptions(threshold=np.inf)
        assert_array_equal(metrix, np.array([[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]],
                                            [[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]]]))

    def test_reshape_auto(self):
        metrix = np.arange(6).reshape(2, -1)
        assert_array_equal(metrix, np.array([[0, 1, 2], [3, 4, 5]]))

if __name__ == '__main__':
    unittest.main()