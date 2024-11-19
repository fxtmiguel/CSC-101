import math
from turtle import color

import data
import utility


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y, other.y) and \
               utility.epsilon_equal(self.z, other.z)

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y, other.y) and \
               utility.epsilon_equal(self.z, other.z)

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'


class Ray:
    # pt is point class and dir is vector class
    def __init__(self, pt, dir):
        self.pt = Point(pt.x, pt.y, pt.z)
        self.dir = Vector(dir.x, dir.y, dir.z)

    def __eq__(self, other):
        return utility.epsilon_equal(self.pt, other.pt) and utility.epsilon_equal(self.dir, other.dir)


class Sphere:
    def __init__(self, center, radius, rgb, finish):
        self.center = Point(center.x, center.y, center.z)
        self.radius = radius
        self.rgb = Color(rgb.r, rgb.g, rgb.b)
        self.finish = finish

    def __eq__(self, other):
        return utility.epsilon_equal(self.center, other.center) and utility.epsilon_equal(self.radius, other.radius)


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return utility.epsilon_equal(self.r, other.r) and utility.epsilon_equal(self.g, other.g) and \
               utility.epsilon_equal(self.b, other.b)

    def __str__(self):
        return f'{int(self.r * 255)} {int(self.g * 255)} {int(self.b * 255)}'


class Finish:
    def __init__(self, ambient, diffuse):
        self.ambient = ambient
        self.diffuse = diffuse

    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient, other.ambient) and utility.epsilon_equal(self.diffuse, other.diffuse)


class Light:
    def __init__(self, pt, color1):
        self.pt = data.Point(pt.x, pt.y, pt.z)
        self.color1 = data.Color(color1.r, color1.g, color1.b)

    def __eq__(self, other):
        return utility.epsilon_equal(self.pt, other.pt) and utility.epsilon_equal(self.color1, other.color1)
