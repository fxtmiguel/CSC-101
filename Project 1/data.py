class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Ray:
    # pt is point class and dir is vector class
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir


class Sphere:
    def __init__(self, center, radius ):
        self.center = center
        self.radius = radius
