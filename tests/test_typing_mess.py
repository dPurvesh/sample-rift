import pytest
from brokenpkg import typing_mess


def test_expects_int_returns_int():
    out = typing_mess.expects_int(1)
    assert isinstance(out, int)  # will fail (string)


def test_returns_dict_values_are_ints():
    d = typing_mess.returns_dict()
    assert all(isinstance(v, int) for v in d.values())  # will fail


def test_duck_raises_attribute_error():
    with pytest.raises(AttributeError):
        typing_mess.duck(object())  # will raise AttributeError (passes)
