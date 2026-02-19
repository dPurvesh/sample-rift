from brokenpkg import io_stuff


def test_read_text_returns_str(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("hello", encoding="utf-8")
    out = io_stuff.read_text(str(p))
    assert isinstance(out, str)  # will fail (bytes)


def test_write_text_writes(tmp_path):
    p = tmp_path / "b.txt"
    io_stuff.write_text(str(p), "x")  # will error writing None
    assert p.read_text(encoding="utf-8") == "x"
