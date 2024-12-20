from typing import Any

# making file to folder as attribute when importing
def __getattr__(key: str) -> Any:
    import importlib

    return importlib.import_module(f"{__name__}.{key}")
