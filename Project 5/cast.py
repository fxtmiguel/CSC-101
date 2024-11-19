import math
import data
import vector_math
import collisions


def cast_ray(ray, sphere_list, color, light, point):
    intersections = collisions.find_intersection_points(sphere_list, ray)
    min_value = math.inf
    min_fin = data.Sphere(data.Point(0, 0, 0), 0, data.Color(0, 0, 0), data.Finish(0.0, 0.0, 0.0, 0.0))
    min_no_inter = data.Color(1.0, 1.0, 1.0)

    intersection_pt = data.Point(0, 0, 0)

    contribute_r = 0
    contribute_g = 0
    contribute_b = 0

    new_r = 0
    new_g = 0
    new_b = 0

    if len(intersections) > 0:
        for j in range(len(intersections)):
            length_vec = data.Point.dist(ray.pt, intersections[j][1])
            if min_value > length_vec:
                min_value = length_vec
                min_fin = sphere_list[j]
                intersection_pt = intersections[j][1]

        normal = collisions.sphere_normal_at_point(min_fin, intersection_pt)
        normal2 = vector_math.scale_vector(normal, 0.01)
        pE = vector_math.translate_point(intersection_pt, normal2)
        l_dir = vector_math.normalize_vector(vector_math.vector_from_to(pE, light.pt))
        light_visible = vector_math.dot_vector(normal, l_dir)

        if light_visible > 0:
            ray1 = data.Ray(pE, l_dir)
            collide = collisions.find_intersection_points(sphere_list, ray1)
            if len(collide) == 0:
                contribute_r = light_visible * light.color.r * min_fin.color.r * min_fin.finish.diffuse
                contribute_g = light_visible * light.color.g * min_fin.color.g * min_fin.finish.diffuse
                contribute_b = light_visible * light.color.b * min_fin.color.b * min_fin.finish.diffuse

        reflection_vector = vector_math.difference_vector(l_dir, vector_math.scale_vector(normal, 2 * light_visible))
        v_dir = vector_math.normalize_vector(vector_math.vector_from_to(point, pE))
        spec_intensity = vector_math.dot_vector(reflection_vector, v_dir)

        if spec_intensity > 0:
            new_r = light.color.r * min_fin.finish.specular * (spec_intensity ** (1 / min_fin.finish.roughness))
            new_g = light.color.g * min_fin.finish.specular * (spec_intensity ** (1 / min_fin.finish.roughness))
            new_b = light.color.b * min_fin.finish.specular * (spec_intensity ** (1 / min_fin.finish.roughness))

        value_r = (min_fin.color.r * color.r * min_fin.finish.ambient) + contribute_r + new_r
        value_g = (min_fin.color.g * color.g * min_fin.finish.ambient) + contribute_g + new_g
        value_b = (min_fin.color.b * color.b * min_fin.finish.ambient) + contribute_b + new_b
        min_no_inter = data.Color(value_r, value_g, value_b)

    return min_no_inter


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
    step_x = (max_x - min_x) / width
    step_y = (max_y - min_y) / height
    for n in range(height):
        for j in range(width):
            x = min_x + (j * step_x)
            y = max_y - (n * step_y)
            pt = data.Point(x, y, 0)
            ray = data.Ray(eye_point, vector_math.vector_from_to(eye_point, pt))
            print(cast_ray(ray, sphere_list, color, light, eye_point))
