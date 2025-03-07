Learn PyPI package

## About

I want to create a PyPI package. Therefore, I need to answer some questions:

- How is a PyPI package structured?
- How is it tested (Unit)? What about static analysis and code style?
- How is it built and published to [PyPI](https://pypi.org)?
- How is it integrated with GitHub Actions?

## Structure
- `src` directory contains source files.
- `tests` directory contains test files
- `pyproject.toml` is a configuration file, to define build system requirements, project metadata, and other settings.

## Code style

- `flake8` package for code linting.
    ```bash
    flake8 src/**/*.py --exclude __init__.py
    ```

- `black` package for code formatting.
    ```bash
    black src/
    black --check src/ 
    ```

- `isort` package for sorting imports.
    ```bash
    isort src/
    isort --check-only src/
    ```

> I consider they are in the category with ESLint and Prettier, but for Python only.


## Testing
- `pytest` package for unit testing.
    ```bash
    poetry run pytest
    ```

## Commands

Test, Build and Publish.
```bash
pip install poetry

poetry install

poetry run pytest

poetry build

poetry config pypi-token.pypi pypi-api-token-here

peotry publish
```
