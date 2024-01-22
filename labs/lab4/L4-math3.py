import math
def rec_area(n, a):
    if(n>2):
        r = a/(2*math.tan(math.pi/n))
        return round(a*n*r/2, 2)
    else:
        print("Your rectangle does not exist")
print(rec_area(int(input("Amount of sides: ")), int(input("Side's length: "))))
