import unittest
import funcs
import objects


class TestCases(unittest.TestCase):
    def test_cases(self):
        a = objects.Point(3, 4)
        self.assertEqual(a.x, 3)
        self.assertEqual(a.y, 4)

    def test_cases2(self):
        a = objects.Circle(4, objects.Point(3, 4))
        self.assertEqual(a.r, 4)
        self.assertEqual(a.c.x, 3)
        self.assertEqual(a.c.y, 4)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
