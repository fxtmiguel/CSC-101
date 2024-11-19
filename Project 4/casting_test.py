import unittest
import data
import cast
import vector_math
import collisions


class Testdata(unittest.TestCase):
    def test_cast_ray_1(self):
        print('P3')
        print(512, 384)
        print('255')
        eye_point = data.Point(0.0, 0.0, -14.0)
        sphere = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0, 0, 1.0), data.Finish(0.2, 1.0))
        sphere_2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0, 0), data.Finish(0.4, 0.7))
        color = data.Color(1.0, 1.0, 1.0)
        light = data.Light(data.Point(1, 0, 2), data.Color(1.0, 0, 0))
        cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, eye_point, [sphere, sphere_2], color, light)


if __name__ == '__main__':
    unittest.main()
