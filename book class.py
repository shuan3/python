class book():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __str__(self):
        return f"{self.a} + {self.b} + {self.c}"
    def __len__(self):
        return self.c
    def __del__(self):
        print("the book has been deleted")
# b=book(1,2,3)
# print(b)
# print(len(b))
# del b



class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        
        volumn=3.14159*self.height*self.radius*self.radius
        return volumn
    
    def surface_area(self):
        area=3.14159*self.radius*self.radius
        print(area)
        return area
c = Cylinder(2,3)
c.volume()
c.surface_area()

