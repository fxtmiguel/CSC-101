import math
import point


def square_all(list1):
    return [x ** 2 for x in list1]


def add_n_all(list1, n):
    new_list = []
    for x in list1:
        new_list.append(x + n)
    return new_list


def distance_all(list1):
    return [math.sqrt((x.x ** 2 + x.y ** 2)) for x in list1]
