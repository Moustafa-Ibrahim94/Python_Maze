import unittest
import Find_Path


class MyTestCase(unittest.TestCase):
    # here i'm checking my intersect_distance function output
    def test_main_function(self):
        result = Find_Path.main_function() # the function output
        corr = [[1, 4], [1, 5], [2, 4], [3, 4], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [7, 6], [7, 7], [8, 7]]
        self.assertEqual(result, corr ) # checking equality


if __name__ == '__main__':
    unittest.main()