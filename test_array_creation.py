import unittest
import numpy as np
from numpy.testing import assert_array_equal

# 配列の生成
class TestArrayCreation(unittest.TestCase):

    # リストからの配列生成
    def test_from_list(self):
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(metrix.shape, (x, x))

    # タプルからの配列生成
    def test_from_tuple(self):
        metrix = np.array(((0, 0, 0), (0, 0, 0)))
        self.assertEqual(metrix.shape, (x, x))

    # zeros関数で配列生成
    def test_zeros_vector(self):
        vector = np.zeros(5)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    # zeros関数で配列生成
    def test_zeros_metrix(self):
        metrix = np.zeros((2, 5))
        assert_array_equal(metrix, np.array([[x, x, x, x, x], [x, x, x, x, x]]))

    # ones関数で配列生成
    def test_ones_vector(self):
        vector = np.ones(5)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    # ones関数で配列生成
    def test_ones_metrix(self):
        metrix = np.ones((2, 5))
        assert_array_equal(metrix, np.array([[x, x, x, x, x], [x, x, x, x, x]]))

    # empty関数で配列生成
    def test_empty(self):
        metrix = np.empty((2, 5))
        self.assertEqual(metrix.shape, (x, x))

    # arange関数で配列生成（to）
    def test_arange_to(self):
        vector = np.arange(5)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    # arange関数で配列生成（from）
    def test_arange_from_to(self):
        vector = np.arange(0, 5)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    # arange関数で配列生成（step）
    def test_arange_with_step(self):
        vector = np.arange(0, 10, 2)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    # linspace関数で配列生成
    def test_linspace(self):
        vector = np.linspace(0, 2, 5)
        assert_array_equal(vector, np.array([x, x, x, x, x]))

    # eye関数で配列生成
    def test_eye(self):
        metrix = np.eye(3)
        assert_array_equal(metrix, np.array([[x, x, x], [x, x, x], [x, x, x]]))

    # identity関数で配列生成
    def test_identify(self):
        metrix = np.identity(3)
        assert_array_equal(metrix, np.array([[x, x, x], [x, x, x], [x, x, x]]))

if __name__ == '__main__':
    unittest.main()
