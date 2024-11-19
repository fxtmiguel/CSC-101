import unittest
import map
import point


class TestCases(unittest.TestCase):
    def test_1(self):
        list1 = [2, 4, 6]
        a = map.square_all(list1)
        b = [4, 16, 36]
        self.assertListEqual(a, b)

    def test_2(self):
        list1 = [9, 10, 32]
        a = map.square_all(list1)
        b = [81, 100, 1024]
        self.assertEqual(a, b)

    def test_add_in(self):
        list1 = [2, 8, 9]
        a = 6
        b = map.add_n_all(list1, a)
        c = [8, 14, 15]
        self.assertEqual(b, c)

    def test_add_in_2(self):
        list1 = [23, 3, 54]
        a = 5
        b = map.add_n_all(list1, a)
        c = [28, 8, 59]
        self.assertEqual(b, c)

    def test_distance(self):
        a = [point.Point(3, 5), point.Point(4, 5), point.Point(6, 9)]
        b = map.distance_all(a)
        c = [5.830951894845301, 6.4031242374328485, 10.816653826391969]
        self.assertEqual(b, c)

    def test_distance_2(self):
        a = [point.Point(9, 2), point.Point(1, 3), point.Point(1, 8)]
        b = map.distance_all(a)
        c = [9.219544457292887, 3.1622776601683795, 8.06225774829855]
        self.assertEqual(b, c)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
