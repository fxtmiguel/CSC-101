def are_positive(list1): return [x for x in list1 if x > 0]


def are_greater_than(list1, n):
    new_list = []
    for i in list1:
        if i > n:
            new_list.append(i)
    return new_list


def are_in_first_quadrant(list1):
    return [x for x in list1 if (x.x > 0) and (x.y > 0)]
