import unittest
import numpy as np

class TestArrayBasic(unittest.TestCase):

    def test_ndim(self):
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.ndim, 1)
        self.assertEqual(metrix.ndim, 2)

    def test_shape(self):
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.shape, (3,))
        self.assertEqual(metrix.shape, (2, 3))

    def test_size(self):
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.size, 3)
        self.assertEqual(metrix.size, 6)

    def test_dtype(self):
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(type(metrix), np.ndarray)
        self.assertEqual(metrix.dtype, np.int64)

if __name__ == '__main__':
    unittest.main()