# CLAUDE.md — Python Project Documentation

## Commands
```bash
python main.py && pytest && ruff check . && mypy src/
```

## Style
- PEP 8, max 79 chars — `PascalCase` classes, `snake_case` funcs/vars, `UPPER_SNAKE` constants
- Type hints everywhere, Google-style docstrings, use `print`

## Test Cases
- Name: `test_<function>_<scenario>_<expected>()`
- Unit → `tests/unit/` · Integration → `tests/integration/` · Coverage ≥ 80%

## Acceptance Checks
- [ ] Tests pass · [ ] No lint errors · [ ] Types valid
- [ ] PEP 8 compliant, line ≤ 79 
