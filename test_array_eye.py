import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayEye(unittest.TestCase):

    def test_eye_NxN(self):
        metrix = np.eye(3)
        assert_array_equal(metrix, np.array([[x, x, x],
                                             [x, x, x],
                                             [x, x, x]]))

    def test_eye_NxM(self):
        metrix = np.eye(2, 3)
        assert_array_equal(metrix, np.array([[x, x, x],
                                             [x, x, x]]))

    def test_eye_k0(self):
        metrix = np.eye(3, k=0)
        assert_array_equal(metrix, np.array([[x, x, x],
                                             [x, x, x],
                                             [x, x, x]]))

    def test_eye_k1(self):
        metrix = np.eye(3, k=1)
        assert_array_equal(metrix, np.array([[x, x, x],
                                             [x, x, x],
                                             [x, x, x]]))

    def test_eye_k1m(self):
        metrix = np.eye(3, k=-1)
        assert_array_equal(metrix, np.array([[x, x, x],
                                             [x, x, x],
                                             [x, x, x]]))

    def test_eye_rot90(self):
        metrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        assert_array_equal(np.rot90(metrix, k=-1),
                          np.array([[x, x, x],
                                    [x, x, x],
                                    [x, x, x]]))

    def test_eye_rot90m(self):
        metrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        assert_array_equal(np.rot90(metrix, k=1),
                          np.array([[x, x, x],
                                    [x, x, x],
                                    [x, x, x]]))

if __name__ == '__main__':
    unittest.main()