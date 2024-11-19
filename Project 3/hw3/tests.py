import unittest
import data
import vector_math


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

    def test_case(self):
        a = data.Vector(4, 5, 6)
        b = data.Vector(12, 15, 18)
        self.assertAlmostEqual(vector_math.scale_vector(a, 3), b)

    def test_case2(self):
        a = data.Vector(1, 2, 3)
        b = data.Vector(1.5, 3, 4.5)
        self.assertAlmostEqual(vector_math.scale_vector(a, 1.5), b)

    def test_dot(self):
        a = data.Vector(4, 5, 6)
        b = data.Vector(2, 4, 1)
        c = data.Vector(8, 20, 6)
        self.assertAlmostEqual(vector_math.dot_vector(a, b), c)

    def test_dot_2(self):
        a = data.Vector(9, 9, 7)
        b = data.Vector(3, 4, 3)
        c = data.Vector(27, 36, 21)
        self.assertAlmostEqual(vector_math.dot_vector(a, b), c)

    def test_length(self):
        a = data.Vector(4, 5, 6)
        self.assertAlmostEqual(vector_math.length_vector(a), 8.77, 2)

    def test_length_2(self):
        a = data.Vector(9, 3, 4)
        self.assertAlmostEqual(vector_math.length_vector(a), 10.295, 2)

    def test_normalize(self):
        a = data.Vector(5.1, 7.1, 9.1)
        b = data.Vector(0.4041640944105519, 0.5626598177088076, 0.7211555410070631)
        self.assertAlmostEqual(vector_math.normalize_vector(a), b)

    def test_normalize_1(self):
        a = data.Vector(8, 20, 6)
        b = data.Vector(0.35777087639996635, 0.8944271909999159, 0.2683281572999748)
        self.assertAlmostEqual(vector_math.normalize_vector(a), b)

    def test_difference_point(self):
        a = data.Point(3, 4, 7)
        b = data.Point(4, 6, 4)
        c = data.Vector(-1, -2, 3)
        self.assertEqual(vector_math.difference_point(a, b), c)

    def test_difference_point_2(self):
        a = data.Point(6, 9, 10)
        b = data.Point(7, 2, 3)
        c = data.Vector(-1, 7, 7)
        self.assertEqual(vector_math.difference_point(a, b), c)

    def test_difference_1(self):
        a = data.Vector(2, 4, 6)
        b = data.Vector(4, 5, 5)
        c = data.Vector(-2, -1, 1)
        self.assertEqual(vector_math.difference_vector(a, b), c)

    def test_difference_2(self):
        a = data.Vector(4, 2, 2)
        b = data.Vector(2, 1, 3)
        c = data.Vector(2, 1, -1)
        self.assertEqual(vector_math.difference_vector(a, b), c)

    def test_translating(self):
        a = data.Point(2, 3, 4)
        b = data.Vector(3, 3, 2)
        c = data.Point(5, 6, 6)
        self.assertEqual(vector_math.translate_point(a, b), c)

    def test_translating_2(self):
        a = data.Point(6, 1, 2)
        b = data.Vector(9, 6, 9)
        c = data.Point(15, 7, 11)
        self.assertEqual(vector_math.translate_point(a, b), c)

    def test_vector_from(self):
        a = data.Vector(2, 4, 5)
        b = data.Vector(4, 6, 9)
        c = data.Vector(2, 2, 4)
        self.assertEqual(vector_math.vector_from_to(a, b), c)

    def test_vector_from_2(self):
        a = data.Vector(5, 9, 11)
        b = data.Vector(6, 8, 4)
        c = data.Vector(1, -1, -7)
        self.assertEqual(vector_math.vector_from_to(a, b), c)


if __name__ == "__main__":
    unittest.main()
