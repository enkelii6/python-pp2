import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("(", self.x, ",", self.y, ")")
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    def dist(self, x2, y2):
        print("distance is:", math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2))

point = Point(int(input("x coordinate:")), int(input("y coordinate:")))
print("coordinates are:")
point.show()
point.move(int(input("How you want x to be moved?")), int(input("And y?")))
print("New coordinates:")
point.show()
point.dist(int(input("2nd point's x:")), int(input("and y:")))

iinp = input()
coords = iinp.split()
p = Point(int(coords[0]), int(coords[1]))
p.show()
