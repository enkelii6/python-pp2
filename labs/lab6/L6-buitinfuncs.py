import functools, time, math
list = map(int, list(input().split()))
print(functools.reduce(lambda x, y: x*y, list))

string = 'iLoVeDaNa'
upper = sum(map(lambda x: x.isupper(), string))
lower = sum(map(lambda x: x.islower(), string))
print(f"Upper: {upper}, lower: {lower}")

string2 = input()
print(string2==string2[::-1])

def root(num, delay):
    time.sleep(delay / 1000)
    return math.sqrt(num)
rootOf = float(input())
ms = float(input())
print(f"Square root of {rootOf} after {ms} miliseconds is {root(rootOf, ms)}")

tuple = (True, True, True, False)
print(all(tuple))
