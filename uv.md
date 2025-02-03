pip install uv


uv init
# add dependencies
uv add typer

uv add --dev pytest


# test
## any file with test will be used to check pytest run
## you can put any import for new package in test.test_main and running below command will auto add package and sovle the dependencies
uv run pytest


## check python
uv run python --version

## change python version -> go to pyproject.toml change python version and run below
uv sync

uv add jupyter pandas  fastapi
uv run jupyer lab

uv tool run

## Lint
uvx ruff check .
uvx ruff check . --fix
uvx ruff format .
