from brokenpkg import state


def test_inc_sequence():
    state.GLOBAL["count"] = 0
    assert state.inc() == 1  # will fail (returns 2)


def test_counter_dec_decrements():
    c = state.Counter(10)
    assert c.dec() == 9  # will fail (returns 11)
