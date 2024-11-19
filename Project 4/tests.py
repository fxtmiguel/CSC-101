import unittest
import data
import cast
import vector_math
import collisions


class Testdata(unittest.TestCase):
    def test_cast_ray(self):
        sphere = data.Sphere(data.Point(2, 0, 0), 1, data.Color(78, 7, 0), data.Finish(0.2))
        sphere2 = data.Sphere(data.Point(53, 0, 0), 1, data.Color(6, 0, 0), data.Finish(0.4))
        sphere_list = [sphere, sphere2]
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(0, 0, 50))
        color = data.Color(1.0, 1.0, 1.0)
        self.assertTrue(cast.cast_ray(ray, sphere_list, color))

    def test_cast_ray_2(self):
        sphere = data.Sphere(data.Point(23, 0, 0), 3, data.Color(5, 24, 8), data.Finish(0.2))
        sphere2 = data.Sphere(data.Point(48, 0, 0), 1, data.Color(28, 23, 0), data.Finish(0.4))
        sphere_list = [sphere, sphere2]
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(0, 0, 20))
        color = data.Color(1.0, 1.0, 1.0)
        self.assertTrue(cast.cast_ray(ray, sphere_list, color))


if __name__ == '__main__':
    unittest.main()
