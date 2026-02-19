import importlib
import pytest


@pytest.mark.parametrize(
    "modname",
    [
        "brokenpkg.syntax_bad_1",
        "brokenpkg.syntax_bad_2",
        "brokenpkg.syntax_bad_3",
    ],
)

def test_modules_have_syntax_errors(modname):
    # These imports should raise SyntaxError by design.
    with pytest.raises(SyntaxError):
        importlib.import_module(modname)
