from typing import Any


def expects_int(x: int) -> int:
    # Intentionally wrong: returns a string
    return "not an int"  # type: ignore[return-value]


def returns_dict() -> dict[str, int]:
    # Intentionally wrong: values are not ints
    return {"a": "1"}  # type: ignore[dict-item]


def duck(a: Any):
    # Intentionally unsafe: assumes attribute exists
    return a.not_a_real_attribute + 1
