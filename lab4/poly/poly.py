def poly_add2(poly1, poly2):
    x = poly1[0] + poly2[0]
    y = poly1[1] + poly2[1]
    z = poly1[2] + poly2[2]
    poly3 = [x, y, z]
    return poly3


def poly_mult2(poly1, poly2):
    x = poly1[0] * poly2[0]
    y = (poly1[0] * poly2[1]) + (poly1[1] * poly2[0])
    z = (poly1[0] * poly2[2]) + (poly1[1] * poly2[1]) + (poly1[2] * poly2[0])
    x_2 = (poly1[2] * poly2[1]) + (poly1[1] * poly2[2])
    y_2 = poly1[2] * poly2[2]
    poly3 = [x, y, z, x_2, y_2]
    return poly3
