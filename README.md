Greet Poetry

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


## Requirements

- Python `3.11`, `3.12`, `3.13`

## Development

Install `poetry` CLI.

```bash
pip install poetry
```

Install project dependencies.

```bash
poetry install
```

Fix code style using `autoflake`, `black` and `isort`.

```bash
poetry run autoflake --in-place --remove-unused-variables -r src/ tests/; poetry run black src/ tests/; poetry run isort src/ tests/;
```

Analyze code using `mypy`.

```bash
poetry run mypy src/ tests/
```

Run tests using `pytest`.

```bash
poetry run pytest
```

Build and publish to `PyPI`.

```bash
poetry build

poetry config pypi-token.pypi <pypi-api-token>

peotry publish
```
