from typing import Any


def __getattr_(key: str) -> Any:
    import importlib

    importlib.import_module(f"{__name__}.{key}")
    # print(f"{__name__}.{key}")


import importlib.util

# def module_from_file(module_name, file_path):
#     spec = importlib.util.spec_from_file_location(module_name, file_path)
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)
#     return module

# foo = module_from_file("cap_text2", "error handling\unittest\scripts\cap.py")
