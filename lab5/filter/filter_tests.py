import unittest
import filter
import point


class TestCases(unittest.TestCase):
    def test_are_positive(self):
        a = [9, -4, 3, -2, 7]
        b = filter.are_positive(a)
        c = [9, 3, 7]
        self.assertEqual(b, c)

    def test_are_positive_2(self):
        a = [4, -6, 2, 4, -1]
        b = filter.are_positive(a)
        c = [4, 2, 4]
        self.assertEqual(b, c)

    def test_are_greater_than(self):
        a = [2, 8, 5, 3, 9, 10]
        b = 5
        c = filter.are_greater_than(a, b)
        new_list = [8, 9, 10]
        self.assertEqual(c, new_list)

    def test_are_greater_than_2(self):
        a = [4, 1, 7, 2, 5, 15]
        b = 4
        c = filter.are_greater_than(a, b)
        new_list = [7, 5, 15]
        self.assertEqual(c, new_list)

    def test_first_quadrant(self):
        a = [point.Point(3, 8), point.Point(7, 2), point.Point(4, -2)]
        b = filter.are_in_first_quadrant(a)
        c = [point.Point(3, 8), point.Point(7, 2)]
        self.assertEqual(b, c)

    def test_first_quadrant_2(self):
        a = [point.Point(1, 4), point.Point(2, -2), point.Point(5, 12)]
        b = filter.are_in_first_quadrant(a)
        c = [point.Point(1, 4), point.Point(5, 12)]
        self.assertEqual(b, c)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
