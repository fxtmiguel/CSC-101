import unittest
import data


class TestData(unittest.TestCase):
    def test_point_1(self):
        a = data.Point(2, 3, 4)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 3)
        self.assertEqual(a.z, 4)

    def test_point_2(self):
        a = data.Point(1, 2, 3)
        self.assertEqual(a.x, 1)
        self.assertEqual(a.y, 2)
        self.assertEqual(a.z, 3)

    def test_vector_1(self):
        a = data.Vector(1, 2, 3)
        self.assertEqual(a.x, 1)
        self.assertEqual(a.y, 2)
        self.assertEqual(a.z, 3)

    def test_vector_2(self):
        a = data.Vector(4, 5, 6)
        self.assertEqual(a.x, 4)
        self.assertEqual(a.y, 5)
        self.assertEqual(a.z, 6)

    def test_ray_1(self):
        a = data.Ray(1, 2)
        self.assertEqual(a.pt, 1)
        self.assertEqual(a.dir, 2)

    def test_ray_2(self):
        a = data.Ray(3, 4)
        self.assertEqual(a.pt, 3)
        self.assertEqual(a.dir, 4)

    def test_sphere_1(self):
        a = data.Sphere(1, 2.5)
        self.assertEqual(a.center, 1)
        self.assertAlmostEqual(a.radius, 2.5)

    def test_sphere_2(self):
        a = data.Sphere(3, 4.5)
        self.assertEqual(a.center, 3)
        self.assertAlmostEqual(a.radius, 4.5)


if __name__ == "__main__":
    unittest.main()
