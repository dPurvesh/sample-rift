import pytest
from brokenpkg import arithmetic


def test_divide_zero_should_raise():
    with pytest.raises(ZeroDivisionError):
        arithmetic.divide(1, 0)  # will fail (returns 0)


def test_mean_basic():
    assert arithmetic.mean([1, 2, 3]) == 2  # will error (IndexError)


def test_add_numbers():
    assert arithmetic.add(1, 2) == 3


def test_add_should_not_concat_strings():
    assert arithmetic.add("1", 2) == 3  # will fail (returns "12")
