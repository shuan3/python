import math


# help(math)
value = 5.35
math.floor(value)
math.ceil(value)

round(4.5)

math.inf
math.nan


import random

# randomly choose between 0 and 100

random.seed(1)
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))


mylist = list(range(0, 20))
# sampleing one element from the list
random.choice(mylist)


# sample with replacement
random.choices(population=mylist, k=10)


# sample without replacement
random.sample(population=mylist, k=10)


random.shuffle(mylist)
random.uniform(a=0, b=100)
