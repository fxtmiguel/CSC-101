import utility
import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y, other.y) and \
               utility.epsilon_equal(self.z, other.z)

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


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
    def __init__(self, pt, dir):
        self.pt = Point(pt.x, pt.y, pt.z)
        self.dir = Vector(dir.x, dir.y, dir.z)

    def __eq__(self, other):
        return utility.epsilon_equal(self.pt, other.x) and utility.epsilon_equal(self.dir, other.y)


class Sphere:
    def __init__(self, center, radius, color, finish):
        self.center = Point(center.x, center.y, center.z)
        self.radius = radius
        self.color = Color(color.r, color.g, color.b)
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
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient, other.ambient) and \
               utility.epsilon_equal(self.diffuse, other.diffuse) and \
               utility.epsilon_equal(self.specular, other.specular) and \
               utility.epsilon_equal(self.roughness, other.roughness)


class Light:
    def __init__(self, pt, color):
        self.pt = pt
        self.color = color

    def __eq__(self, other):
        return utility.epsilon_equal(self.pt, other.pt) and utility.epsilon_equal(self.color, other.color)
