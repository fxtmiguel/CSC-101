import utility


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
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        return utility.epsilon_equal(self.pt, other.x) and utility.epsilon_equal(self.dir, other.y)


class Sphere:
    def __init__(self, center, radius, ):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        return utility.epsilon_equal(self.center, other.x) and utility.epsilon_equal(self.radius, other.y)
