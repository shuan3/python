import importlib

key = "module_a"  # This can be dynamically set to "module_a" or "module_b"
key = "time"
try:
    module = importlib.import_module(f"{__name__}.{key}")
    print(f"Successfully imported {module}")
except ModuleNotFoundError:
    print(f"Module {key} not found.")
