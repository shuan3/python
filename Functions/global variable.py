x = 50


def func():
    global x
    print(f"x is {x}")
    x = "NEW VALUE"
    print(f" glocal is {x}")

    # return x


func()
print(x)
