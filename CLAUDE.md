# Project conventions (CT template)

Read this before changing anything. Rules marked *enforced* are checked by the platform
and fail the step if broken; the rest are checked by the reviewers.

## Stack and dependencies
- Python 3.13, standard library only.
- Add no dependency unless an approved design names it.

## Layout
- Code lives in `src/` as plain modules (`src/<module>.py`); no packages or new top-level folders.
- Tests live in `tests/test_<module>.py`, one file per module.

## Coding conventions
- Type-annotate every public function and give it a one-line docstring.
- Validate inputs where they enter and raise `ValueError` or `TypeError` with a message naming the
  bad value; don't return `None` or `-1` to signal an error.
- No mutable global state, no `print` in library code, no bare `except`.
- Lint-clean at line length 110 (*enforced*: ruff in the Self-test gate).

## Testing
- Every public function has pytest tests for normal cases, edge cases and each error it raises.
- Tests are deterministic: no network, no sleeps, no dependence on the clock or test order.
- Never delete, skip or weaken an existing test to make the checks pass (*enforced*: protect_tests).
- `python -m pytest -q` passes (*enforced*: the Self-test gate).

## Boundaries
- Change only the files your requirement needs; other developers work on this repo in parallel.
- Don't edit CLAUDE.md, `pyproject.toml` or CI config unless the requirement is about them.
- Don't commit or merge; the platform commits your changes and merges approved work.

## Security
- No secrets, tokens or credentials in code, tests or logs.
- No `eval`/`exec`, no `shell=True` with interpolated input, no unpickling untrusted data.
