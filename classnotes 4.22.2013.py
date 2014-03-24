class Animal():
    def __init__(self,name):
        self.myname = name
        
    def noise(self):
        return 'I am silent'
    
    def getName(self):
        return self.myname

class Dog(Animal):
    def noise(self):
        return 'Woof, woof'
    
class Cat(Animal):
    def __init__(self,name,temper='Cuddly'):
        self.myname = name
        self.mytemper = temper
class Kitten(Cat):
    def noise(self):
        return 'Meeeeeeeeew'