import math
import data


def scale_vector(vector, scalar): return data.Vector(vector.x * scalar, vector.y * scalar, vector.z * scalar)


def dot_vector(vector1, vector2): return data.Vector((vector1.x * vector2.x), (vector1.y * vector2.y), (
        vector1.z * vector2.z))


def length_vector(vector): return math.sqrt((vector.z ** 2 + vector.x ** 2 + vector.y ** 2))


def normalize_vector(vector): return scale_vector(vector, 1 / (length_vector(vector)))


def difference_point(point1, point2): return data.Vector(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)


def difference_vector(vector1, vector2): return data.Vector(vector1.x - vector2.x, vector1.y - vector2.y,
                                                            vector1.z - vector2.z)


def translate_point(point, vector): return data.Point(point.x + vector.x, point.y + vector.y, point.z + vector.z)


def vector_from_to(from_point, to_point): return difference_point(to_point, from_point)
