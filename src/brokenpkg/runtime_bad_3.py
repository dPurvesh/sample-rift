def recursion():
    # Intentionally infinite recursion
    return recursion()


def value_error():
    return int("not-a-number")


def assert_fail():
    assert 2 + 2 == 5
