from pathlib import Path

# d:\Github\test
print(Path.cwd())
# C:\Users\shanh
print(Path.home())


# d:\Github
print(Path.cwd().parents[0])
print(Path.cwd().parents[0] / "Output")
# d:\Github\test\Path\path.py
print(Path(__file__))

"""
['d:\\Github\\test\\Path', 'C:\\Users\\shanh\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip',
 'C:\\Users\\shanh\\AppData\\Local\\Programs\\Python\\Python312\\DLLs',
 'C:\\Users\\shanh\\AppData\\Local\\Programs\\Python\\Python312\\Lib',
 'C:\\Users\\shanh\\AppData\\Local\\Programs\\Python\\Python312',
 'C:\\Users\\shanh\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages',
 'C:\\Users\\shanh\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\win32',
 'C:\\Users\\shanh\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\win32\\lib',
'C:\\Users\\shanh\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\Pythonwin']
"""
import sys

# print(sys.path)
# add search path for python
# sys.path.append('.../../')


from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))

sys.path.append(d)
print(sys.path)
