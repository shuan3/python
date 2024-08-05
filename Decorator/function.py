def func():
    return 1
#how to return function

def dec(name="a"):
    def greet():
        return '\t This is  the greet()'
    def welcome():
        return '\t This is  the welcome()'
    print('I am going to return a functions!!')

    if name == 'a':
        return greet
    else:
        return welcome

# lol=dec(name="a")
# print(lol())


#how to pass function inside a function
def hello():
    print("hello")
def some_def_func():
    print("some def func")
def other(some_def_func):
    print("other codes runs here!")
    print(some_def_func())

# other(hello)





#create decorator
def new_decorator(func):
    def wrap_func():
        print('some extra code, before the original func')
        func()
        print('some extra code, after the original func')

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("I want to be decorated")
func_needs_decorator()
# new_decorator(hello)