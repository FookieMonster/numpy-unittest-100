import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArraySlicing(unittest.TestCase):

    def test_indexing_1d(self):
        vector = np.arange(10)
        self.assertEqual(vector[0], x)

    def test_indexing_2d(self):
        metrix = np.arange(9).reshape(3, 3)
        self.assertEqual(metrix[0][0], 0)
        self.assertEqual(metrix[0, 0], 0)
        assert_array_equal(metrix[0], np.array([x, x, x]))
        assert_array_equal(metrix[1], np.array([x, x, x]))
        assert_array_equal(metrix[2], np.array([x, x, x]))

    def test_fancy_indexing(self):
        vector = np.array([7, 6, 5])
        assert_array_equal(vector[[2, 0, 1]], np.array([x, x, x]))

    def test_indexing_with_boolean_arrays(self):
        metrix = np.arange(9).reshape(3, 3)
        assert_array_equal(metrix > 4, np.array([[x, x, x],
                                                 [x, x, x],
                                                 [x, x, x]]))

    def test_indexing_with_selected_elements(self):
        metrix = np.arange(9).reshape(3, 3)
        assert_array_equal(metrix[metrix > 4], np.array([x, x, x, x]))

    def test_indexing_with_assignments(self):
        metrix = np.arange(9).reshape(3, 3)
        metrix[metrix > 4] = 0
        assert_array_equal(metrix, np.array([[x, x, x],
                                             [x, x, x],
                                             [x, x, x]]))

if __name__ == '__main__':
    unittest.main()