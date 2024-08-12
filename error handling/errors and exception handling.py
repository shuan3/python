def add(*args):
    s = 0
    for i in args:
        s = i + s
    return s


try:
    add(1, 2, 3, 4, 5, 6, 7, 8, 9, "10")
except TypeError:
    print("error")
except OSError:
    print("os error")
else:
    print("else")
finally:
    print("finally done")
