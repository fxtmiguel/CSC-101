import unittest

import collisions
import data
from collisions import *


class TestCases2(unittest.TestCase):
    def test_sphere_intersection_point1(self):
        self.assertEqual(sphere_intersection_point(data.Ray(data.Point(2, 0, 0), data.Vector(8, 0, 0)),
                                                   data.Sphere(data.Point(7, 0, 0), 4)), data.Point(3, 0, 0))

    def test_sphere_intersection_point2(self):
        ray = data.Ray(data.Point(2.4, 1, 0), data.Vector(6, 2.5, 0))
        sphere = data.Sphere(data.Point(12, 5, 0), 3)
        intersection = sphere_intersection_point(ray, sphere)
        self.assertEqual(intersection, data.Point(9.23076, 3.84615, 0))

    def test_sphere_intersection_point3(self):
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(3, 12, 4))
        sphere = data.Sphere(data.Point(3, 12, 4), 2)
        intersection = sphere_intersection_point(ray, sphere)
        self.assertEqual(intersection, data.Point(2.53846, 10.15384, 3.38461))

    def test_intersection_point(self):
        x1 = data.Sphere(data.Point(4, 0, 8), 6)
        x2 = data.Sphere(data.Point(5, 4, 0), 7)
        x_list = [x1, x2]
        ray = data.Ray(data.Point(3, 5, 6), data.Vector(4, 0, 0))
        new_point = collisions.find_intersection_points(x_list, ray)
        self.assertEqual(new_point[0][1], data.Point(6.645751311064591, 5.0, 6.0))

    def test_intersection_point_1(self):
        x1 = data.Sphere(data.Point(7, 2, 0), 5)
        x2 = data.Sphere(data.Point(9, 3, 3), 3)
        x_list = [x1, x2]
        ray = data.Ray(data.Point(2.5, 0, 2), data.Vector(4, 0, 0))
        new_point = collisions.find_intersection_points(x_list, ray)
        self.assertEqual(new_point[0][1], data.Point(2.8768943743823394, 0.0, 2.0))

    def test_sphere_normal(self):
        sphere = data.Sphere(data.Point(2.5, 5.3, 3.4), 5)
        point = data.Point(5.6, 7.4, 3.5)
        new = collisions.sphere_normal_at_point(sphere, point)
        self.assertAlmostEqual(new.x, 0.827, 2)
        self.assertAlmostEqual(new.y, 0.56, 2)
        self.assertAlmostEqual(new.z, 0.026, 2)

    def test_sphere_normal_2(self):
        sphere = data.Sphere(data.Point(1.4, 3.3, 5.2), 9)
        point = data.Point(9.4, 5.5, 4.3)
        new = collisions.sphere_normal_at_point(sphere, point)
        self.assertAlmostEqual(new.x, 0.958, 2)
        self.assertAlmostEqual(new.y, 0.263, 2)
        self.assertAlmostEqual(new.z, -0.107, 2)



if __name__ == '__main__':
    unittest.main()
