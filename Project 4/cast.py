import collisions
import data
import vector_math
import math


def cast_ray(ray, sphere_list, color, light):
    intersections = collisions.find_intersection_points(sphere_list, ray)
    min_value = math.inf
    min_sphere = data.Sphere(data.Point(0, 0, 0), 0, data.Color(0, 0, 0), data.Finish(0.0, 0.0))
    total = data.Color(1.0, 1.0, 1.0)
    # off_point =
    if len(intersections) > 0:
        for n in range(len(intersections)):
            length_vec = data.Point.dist(ray.pt, intersections[n][1])
            Pe = vector_math.translate_point(collisions.find_intersection_points(sphere_list[n], ray), (
                vector_math.scale_vector(collisions.sphere_normal_at_point(sphere_list[n], intersections[n][1]), 0.01)))
            if min_value > length_vec:
                min_value = length_vec
                min_sphere = sphere_list[n]
        value_r = min_sphere.rgb.r * color.r * min_sphere.finish.ambient * min_sphere.finish.diffuse
        value_g = min_sphere.rgb.g * color.g * min_sphere.finish.ambient * min_sphere.finish.diffuse
        value_b = min_sphere.rgb.b * color.b * min_sphere.finish.ambient * min_sphere.finish.diffuse
        total = data.Color(value_r, value_g, value_b)
    return total


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
    step_x = (max_x - min_x) / width
    step_y = (max_y - min_y) / height
    for n in range(height):
        for i in range(width):
            x = min_x + (i * step_x)
            y = max_y - (n * step_y)
            pt = data.Point(x, y, 0)
            ray = data.Ray(eye_point, vector_math.vector_from_to(eye_point, pt))
            print(cast_ray(ray, sphere_list, color, light))
