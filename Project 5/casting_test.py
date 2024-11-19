import data
import cast
import vector_math
import collisions

width = 512
height = 384
print('P3')
print(width, height)
print(255)

eye_point = data.Point(0.0, 0.0, -14.0)
sphere1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0.0, 0.0, 1.0), data.Finish(0.2, 1.0, 0.5, 0.05))
sphere2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0.0, 0.0), data.Finish(0.4, 0.7, 0.5, 0.05))
sphere_l = [sphere1, sphere2]
light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, eye_point, sphere_l, data.Color(1.0, 1.0, 1.0), light)