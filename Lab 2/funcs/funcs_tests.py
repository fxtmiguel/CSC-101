import unittest
import funcs


class TestCases(unittest.TestCase):
    def test_square(self):
        pass

    def test_f(self):
        a = funcs.f(2)
        b = funcs.f(1)
        self.assertEqual(a, 32)
        self.assertEqual(b, 9)

    def test_g(self):
        a = funcs.g(1, 2)
        b = funcs.g(3, 4)
        self.assertEqual(a, 5)
        self.assertEqual(b, 25)

    def test_hyp(self):
        a = funcs.hypotenuse(3,5)
        b = funcs.hypotenuse(2, 3)
        self.assertAlmostEqual(a, 28)
        self.assertAlmostEqual(b, 11)

    def test_pos(self):
        a =funcs.is_positive(5)
        b =funcs.is_positive(-3)
        self.assertTrue(a)
        self.assertFalse(b)
# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
