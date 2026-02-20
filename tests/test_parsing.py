import pytest
from brokenpkg import parsing


def test_parse_json_dict():
    assert parsing.parse_json('{"a": 1}') == {"a": 1}  # will error


def test_parse_int_rejects_float_string():
    with pytest.raises(ValueError):
        parsing.parse_int("1.5")  # will not raise (returns 1)


def test_split_csv_quotes():
    line = 'a,"b,c",d'
    assert parsing.split_csv_line(line) == ["a", "b,c", "d"]  # will fail
