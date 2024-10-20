from typing import Any


def __getattr__(key: str) -> Any:
    import importlib

    return importlib.import_module(f"{__name__}.{key}")
