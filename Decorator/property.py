class get_email:
    def __init__(self,fn,ln):
        self.fn=fn
        self.ln=ln
    def email(self):
        return f'{self.fn}.{self.ln}@lol.com'
    
kk=get_email('super','man')
print(kk.email())
#property will enabled the dynamic changing part
class get_email2:
    def __init__(self,fn,ln):
        self.fn=fn
        self.ln=ln
    @property
    def email(self):
        return f'{self.fn}.{self.ln}@lol.com'
    
kk=get_email('super','man')
kk.fn='homelander'
print(kk.email())





class get_email2:
    def __init__(self,fn,ln):
        self.fn=fn
        self.ln=ln
    @property
    def email(self):
        return f'{self.fn}.{self.ln}@lol.com'
    @property
    def fullname(self):
        return f'{self.fn}.{self.ln}'
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.fn=first
        self.ln=last
    @fullname.deleter
    def fullname(self):
        self.fn=None
        self.ln=None 
kk=get_email('super','man')
kk.fullname='homelander ss'
print(kk.fullname)
# del kk.fullname
# print(kk.fullname)