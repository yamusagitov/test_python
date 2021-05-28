# inheritance - наследование - inheritage
# heritage - наследство

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass
    
class Cat(Mammal):
    pass

first = Dog()
first.walk()

second = Cat()
second.walk()