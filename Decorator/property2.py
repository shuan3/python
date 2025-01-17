class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        print("Getting radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Setting radius")
        if value == 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        if self._area is None:
            print("Calculating area")
            self._area = 3.14159 * (self.radius**2)
            print(self._area)
        return self._area


c = Circle(5)
print(c.radius)
print(c.area)


class Myclass:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_string(cls, string):
        value = int(string)
        return cls(value)


print(Myclass.from_string("10").value)
