class Shape():
    def area(self):
        print("area equals 0")

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print("area equals", self.length**2)

print("Enter the length of your square:")
x = Square(int(input()))
a = Shape()
x.area()
a.area()

"""
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        print("area equals", self.length * self.width
print("Enter length and width")
r = Rectangle(int(input()), int(input())
r.area()
"""