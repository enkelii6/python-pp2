import math
def squares(n):
    i = 1
    while i**2 <= n:
        yield i**2
        i+=1
n = int(input())
gen = squares(n)
for value in gen:
    print(value)
