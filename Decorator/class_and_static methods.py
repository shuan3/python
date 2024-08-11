
# Class Method vs Static Method
# The basic difference between the class method vs Static method in Python and when to use the class method and static method in Python.

# A class method takes class as the first parameter while a static method needs no specific parameters.
# A class method can access or modify the class state while a static method can’t access or modify it.
# In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# We use @classmethod decorator in Python to create a class method and we use @staticmethod decorator to create a static method in Python.

class calculator:

    def __init__(self,version):
        self.version=version
    def display(self):
        print(f'Current version is {self.version}')

    @staticmethod
    def add_numbers(self,*nums):
        print(sum(nums))
        return sum(nums)
#staticmethod will by pass init variable and add_numbers is like individual function. The args provided is only accepted by add_numbers()
# print(calculator.add_numbers(1,2,3))

import datetime
class Person:
    def __init__(self,name:str,age:str):
        self.name=name
        self.age=age
    def description(self):
        return f'{self.name} is {self.age} year old'
    
    @classmethod
    def age_from_year(cls,name,birth_year):
        current_year=datetime.date.today().year
        age=current_year-birth_year
        return cls(name,age)


# if __name__=='__main__':
#     lol=Person.age_from_year('Federico',1997)
#     print(lol.description())



class Geeks:
    course = 'DSA'
    list_of_instances = []

    def __init__(self, name):
        self.name = name
        Geeks.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"

    @staticmethod
    def welcome_message():
        return "Welcome to Geeks for Geeks!"

# Creating instances
g1 = Geeks('Alice')
g2 = Geeks('Bob')

# Calling class methods
print(Geeks.get_course(),'1')  
print(Geeks.get_instance_count(),'2')  

# Calling static method
print(Geeks.welcome_message(),'3') 






