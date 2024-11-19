import math


def f(x):
    return 7 * math.pow(x, 2) + (2 * x)


def g(x, y):
    return math.pow(x, 2) + (math.pow(y, 2))


def hypotenuse(leg1, leg2):
    return math.sqrt(math.pow(leg1, 2)) + (math.pow(leg2, 2))


def is_positive(x):
    return x > 0
