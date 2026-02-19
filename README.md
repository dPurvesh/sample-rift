# broken-python-repo

Intentionally broken Python-only codebase for testing:

- Some modules contain **syntax errors** (cannot import).
- Some functions raise **runtime exceptions**.
- Tests are **intentionally failing**.

Run:
```bash
python -m pytest -q
```
