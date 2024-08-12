import unittest

# import importlib
from scripts.cap import cap_text2

# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'scripts')))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# def module_from_file(module_name, file_path):
#     spec = importlib.util.spec_from_file_location(module_name, file_path)
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)
#     return module

# foo = module_from_file("cap_text2", "unittest\scripts\cap.py")


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = "python"
        result = cap_text2(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "monty python"
        result = cap_text2(text)
        self.assertEqual(result, "Monty Python")


if __name__ == "__main__":
    unittest.main()
