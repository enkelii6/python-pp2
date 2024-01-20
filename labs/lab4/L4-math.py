import math
def angle_radians(degrees):
    return degrees * 0.017453
print(angle_radians(float(input("Input degree: "))))
def tr_area(a, b, h):
    return (a+b)/2 * h
print(tr_area(int(input("Base 1: ")), int(input("Base 2: ")), int(input("Height: "))))
def rec_area(n, a):
    if(n>2):
        r = a/(2*math.tan(math.pi/n))
        return round(a*n*r/2, 2)
    else:
        print("Your rectangle does not exist")
print(rec_area(int(input("Amount of sides: ")), int(input("Side's length: "))))
def par_area(b, h):
    return b*h
print(par_area(int(input("Base: ")), int(input("Height: "))))