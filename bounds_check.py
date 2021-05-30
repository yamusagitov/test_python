class BoundsChecker:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def isBounded(self, val):
        return self.min_value <= val <= self.max_value 

checker = BoundsChecker(10, 50)
x = int(input('>'))


if (checker.isBounded(x)):
    print (f" {x} is good")

else:
    print (f"Your {x} is not eligible")

