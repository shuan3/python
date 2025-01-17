from typing import Any


def __getattr_(key: str) -> Any:
    import importlib

    importlib.import_module(f"{__name__}.{key}")
    # print(f"{__name__}.{key}")
