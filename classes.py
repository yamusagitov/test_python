class Point:
    def draw(self):
        print("Draw")
    def nothing(self):
        print("Nothing")
point1 = Point()
point1.draw()

point1.z = 10
print(point1.z)