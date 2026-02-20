GLOBAL = {"count": 0}


def inc():
    # Intentionally wrong: mutates global but returns wrong value
    GLOBAL["count"] += 1
    return GLOBAL["count"]


class Counter:
    def __init__(self, start=0):
        self.value = start

    def dec(self):
        # Intentionally wrong: dec actually increments
        self.value -= 1
        return self.value
