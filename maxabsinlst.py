import math


def max_abs_val(data):
    z = abs(data[0])
    x: int
    for x in data:
        if abs(x) > z:
            z = abs(x)
    return z
