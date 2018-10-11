import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayCreation(unittest.TestCase):

    def test_from_list(self):
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(metrix.shape, (x, x))

    def test_from_tuple(self):
        metrix = np.array(((0, 0, 0), (0, 0, 0)))
        self.assertEqual(metrix.shape, (x, x))

    def test_zeros_vector(self):
        vector = np.zeros(5)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_zeros_metrix(self):
        metrix = np.zeros((2, 5))
        assert_array_equal(metrix, np.array([[x, x, x, x, x], [x, x, x, x, x]]))

    def test_ones_vector(self):
        vector = np.ones(5)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_ones_metrix(self):
        metrix = np.ones((2, 5))
        assert_array_equal(metrix, np.array([[x, x, x, x, x], [x, x, x, x, x]]))

    def test_empty(self):
        metrix = np.empty((2, 5))
        self.assertEqual(metrix.shape, (x, x))

    def test_arange_to(self):
        vector = np.arange(5)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_arange_from_to(self):
        vector = np.arange(0, 5)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_arange_step(self):
        vector = np.arange(0, 10, 2)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_linspace(self):
        vector = np.linspace(0, 2, 5)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    def test_eye(self):
        metrix = np.eye(3)
        assert_array_equal(metrix, np.array([[x, x, x], [x, x, x], [x, x, x]]))

    def test_identify(self):
        metrix = np.identity(3)
        assert_array_equal(metrix, np.array([[x, x, x], [x, x, x], [x, x, x]]))

if __name__ == '__main__':
    unittest.main()