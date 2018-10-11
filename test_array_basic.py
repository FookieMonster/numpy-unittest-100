import unittest
import numpy as np

class TestArrayBasic(unittest.TestCase):

    def test_ndim(self):
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.ndim, x)
        self.assertEqual(metrix.ndim, x)

    def test_shape(self):
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.shape, (x,))
        self.assertEqual(metrix.shape, (x, x))

    def test_size(self):
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.size, x)
        self.assertEqual(metrix.size, x)

    def test_dtype(self):
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(type(metrix), x)
        self.assertEqual(metrix.dtype, x)

if __name__ == '__main__':
    unittest.main()