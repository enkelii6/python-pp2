import time, math
def root(num, delay):
    time.sleep(delay / 1000)
    return math.sqrt(num)
rootOf = float(input())
ms = float(input())
print(f"Square root of {rootOf} after {ms} miliseconds is {root(rootOf, ms)}")
