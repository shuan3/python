import random
import numpy as np

print(np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0]))

# Python program to explain property()
# function using decorator


class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    @property
    def value(self):
        print("Getting value")
        return self._value

    # setting the values
    @value.setter
    def value(self, value):
        print("Setting value to " + value)
        self._value = value

    # deleting the values
    @value.deleter
    def value(self):
        print("Deleting value")
        del self._value


# passing the value
x = Alphabet("Peter")
print(x.value)

x.value = "Diesel"

print("check here", 0.9 // 1)
