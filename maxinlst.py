def max_val(data):
    z = data[0]
    x: int
    for x in data:
        if x > z:
            z = x
    return z
