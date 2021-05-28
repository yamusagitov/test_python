class Point:
    
    # constructor
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

point = Point(10, 20)
print(point.x)
point.move()

class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
john.talk()

bob = Person("Bob Peterson")
bob.talk()