def key_error():
    d = {}
    return d["missing"]


def type_error():
    return 1 + "2"


def attr_error():
    return None.missing  # type: ignore[union-attr]
