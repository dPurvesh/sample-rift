from pathlib import Path


def read_text(path: str) -> str:
    # Intentionally wrong: uses binary mode but returns bytes sometimes.
    p = Path(path)
    with p.open("rb") as f:
        data = f.read()
    return data  # returning bytes, not str


def write_text(path: str, content: str) -> None:
    # Intentionally wrong: attempts to write None.
    p = Path(path)
    with p.open("w", encoding="utf-8") as f:
        f.write(None)  # type: ignore[arg-type]
