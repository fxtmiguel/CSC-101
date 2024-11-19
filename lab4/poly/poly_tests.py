import unittest
import poly


class TestPoly(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_poly_add(self):
        poly1 = [3, 2, 7.4]
        poly2 = [2, 4, 6.4]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [5, 6, 13.8])

    def test_poly_add2(self):
        poly1 = [7, 3, 9.4]
        poly2 = [4, 5.6, 3.2]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [11, 8.6, 12.6])

    def test_mult2(self):
        poly1 = [3, 5, 19.4]
        poly2 = [3, 4, 13.2]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [9, 27, 117.79999999999998, 143.6, 256.08])

    def test_mult2_2(self):
        poly1 = [5, 4.5, 89.3]
        poly2 = [4.5, 5.3, 84.3]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [22.5, 46.75, 847.2, 852.6399999999999, 7527.99])


if __name__ == '__main__':
    unittest.main()
