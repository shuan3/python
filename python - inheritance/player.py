class Person():
    def __init__(self,name,age,city):
        self.age=age
        self.name=name
        self.city=city
    def introduction(self):
        return f'I am {self.name} and I am {self.age}'
#Example 1
# class Player(Person):
#     pass

# player1=Player('Joe',45,'Londo')
# print(player1.age)

#Example 2
# class Player(Person):
#     def __init__(self,name,age,city):
#         print('Player init')
#         self.age=age
#         self.name=name
#         self.city=city

# player1=Player('Joe',45,'Londo')
# print(player1.introduction())

#Example 3
# class Player(Person):
#     def __init__(self,name,age,city,level):
#         super().__init__(name,age,city)
#         print('Player init')
#         self.level=level
#     def introduction(self):
#         print('Player introduction')
#         # return super().introduction()
#         return f'lol'


# Example 4
class Person():
    def __init__(self,name,age,city,*args,**kwargs):
        self.age=age
        self.name=name
        self.city=city
    def introduction(self,*args,**kwargs):
        return f'I am {self.name} and I am {self.age}'
class Player(Person):
    def __init__(self,name,age,city,level,*args,**kwargs):
        super().__init__(name,age,city,*args,**kwargs)
        print(f'Player init child class ')
        print(*args,**kwargs)
        a=kwargs.get('a',0)
        print(f'a is {a}',args[0])
        self.level=level
    def introduction(self):
        print('Player introduction')
        # return super().introduction()
        return f'lol'
    


player1=Player('Joe',45,'Londo',10,1,1,{'a':1})
print(player1.introduction())
print(player1.level)