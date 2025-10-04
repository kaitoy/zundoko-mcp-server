# Agent Guidelines

## Build/Test Commands
- Install dependencies: `pip install -r requirements.txt` or `uv install`
- Run tests: `pytest` or `python -m pytest`
- Single test: `pytest tests/test_file.py::test_function_name`
- Lint: `ruff check` or `flake8`
- Format: `ruff format` or `black .`
- Type check: `mypy` or `pyright`

## Code Style Guidelines
- Follow PEP 8 style guide
- Use snake_case for functions/variables, PascalCase for classes
- Use type hints for all function signatures and class attributes
- Import order: standard library, third-party, local imports (separated by blank lines)
- Use f-strings for string formatting
- Handle exceptions explicitly with try/except blocks
- Use pathlib.Path for file system operations
- Prefer list/dict comprehensions over loops when readable
- Add docstrings for all public functions and classes
- Use dataclasses or Pydantic models for structured data

## Testing
- Write tests for all new features and bug fixes
- Use descriptive test function names starting with `test_`
- Use pytest fixtures for test setup and teardown
- Mock external dependencies with unittest.mock or pytest-mock
- Organize tests in a `tests/` directory mirroring the source structure

*Note: Update this file as the project structure and conventions become established.*