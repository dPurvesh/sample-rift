def boom():
    raise RuntimeError("intentional boom")


def div_zero():
    return 1 / 0


def index_error():
    a = []
    return a[1]
