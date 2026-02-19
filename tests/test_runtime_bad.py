import pytest
from brokenpkg import runtime_bad_1, runtime_bad_2, runtime_bad_3


def test_boom_raises():
    with pytest.raises(RuntimeError):
        runtime_bad_1.boom()


def test_div_zero_raises():
    with pytest.raises(ZeroDivisionError):
        runtime_bad_1.div_zero()


def test_type_error_raises():
    with pytest.raises(TypeError):
        runtime_bad_2.type_error()


def test_assert_fail_fails():
    # This test is intentionally "wrong": it expects no failure but function asserts.
    runtime_bad_3.assert_fail()  # will fail the test
