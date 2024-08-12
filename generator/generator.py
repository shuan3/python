# def create_cubes(n):
#     result=[]
#     for x in range(n):
#         result.append(x**3)
#     return result
# for x in create_cubes(10):
#     print(x)
def create_cubes(n):
    for x in range(n):
        yield x**3


# list(create_cubes(10))
for x in create_cubes(10):
    print(x)


# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3


for x in gencubes(10):
    print(x)

s = "hello"
ss = iter(s)
print(next(ss))
print(next(ss))
