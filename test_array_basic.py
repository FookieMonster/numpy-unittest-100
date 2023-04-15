import unittest
import numpy as np

# NumPyの基礎
class TestArrayBasic(unittest.TestCase):

    # 配列の軸数（次元数）
    def test_ndim(self):
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.ndim, x)
        self.assertEqual(metrix.ndim, x)

    # 配列の形状
    def test_shape(self):
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.shape, (x,))
        self.assertEqual(metrix.shape, (x, x))

    # 配列の総要素数
    def test_size(self):
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.size, x)
        self.assertEqual(metrix.size, x)

    # 配列の要素の型
    def test_dtype(self):
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(type(metrix), x)
        self.assertEqual(metrix.dtype, x)

if __name__ == '__main__':
    unittest.main()
