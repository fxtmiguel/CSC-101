import math
import objects


def distance(point_a, point_b):
    return math.sqrt(math.pow(point_b.x - point_a.x, 2) + math.pow(point_b.y - point_a.y, 2))


def circles_overlap(circle_a, circle_b):
    dist = distance(circle_a.center, circle_b.center)

    if dist < (circle_a.r + circle_b.r):
        return True

    return False
