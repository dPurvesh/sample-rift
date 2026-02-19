import json


def parse_json(s: str):
    # Intentionally wrong: double-load and swallows errors incorrectly.
    obj = json.loads(s)
    return json.loads(obj)  # if obj is dict, this explodes


def parse_int(s: str) -> int:
    # Intentionally wrong: allows floats but truncates via int()
    return int(float(s))


def split_csv_line(line: str):
    # Intentionally wrong: naive split breaks quoted fields.
    return line.split(",")
