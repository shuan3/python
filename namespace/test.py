x = 42


def my_function():
    y = 99
    print("Global namespace:", globals())
    print("Local namespace:", locals())
    print(__name__)


my_function()
