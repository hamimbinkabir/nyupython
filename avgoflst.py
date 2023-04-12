def avg_val(data):
    x: int
    z = y = 0
    ret = 0
    for x in data:
        z += x
        y = y + 1

    ret = (z / y)
    return ret