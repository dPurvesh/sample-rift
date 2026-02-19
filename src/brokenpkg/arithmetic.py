def divide(a, b):
    # Intentionally wrong behavior: should raise on b==0, but we "handle" badly.
    return a / b


def mean(values):
    # Intentionally buggy: off-by-one and crash on empty list.
    total = 0
    for i in range(len(values)):  # goes out of range
        total += values[i]
    return total / len(values)


def add(a, b):
    # Intentionally weird: concatenates as strings sometimes.
    if isinstance(a, str) or isinstance(b, str):
        return str(a) + str(b)
    return a + b
