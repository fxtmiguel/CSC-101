import math
import data
import vector_math


def sphere_intersection_point(ray, sphere):
    diff = vector_math.difference_point(ray.pt, sphere.center)
    a = vector_math.dot_vector(ray.dir, ray.dir)
    b = 2 * vector_math.dot_vector(diff, ray.dir)
    c = (vector_math.dot_vector(diff, diff) - sphere.radius ** 2)
    discriminant = (b ** 2) - 4 * a * c

    if discriminant < 0:
        return None

    elif discriminant > 0:
        t1 = (-b + math.sqrt(discriminant)) / (2 * a)
        t2 = (-b - math.sqrt(discriminant)) / (2 * a)

        if t1 >= 0 and t2 >= 0:
            t = min(t1, t2)

        elif (t1 >= 0 and t2 <= 0) or (t1 <= 0 and t2 >= 0):
            t = max(t1, t2)

        else:
            return None
    else:
        t = -b / (2 * a)
        if t < 0:
            return None

    point_translate = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t))
    return point_translate


def find_intersection_points(sphere_list, ray):
    intersects = []
    for n in sphere_list:
        point = sphere_intersection_point(ray, n)
        if point is not None:
            intersects.append((n, sphere_intersection_point(ray, n)))
    return intersects


def sphere_normal_at_point(sphere, point):
    return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
