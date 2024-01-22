import functools
list = map(int, list(input().split()))
print(functools.reduce(lambda x, y: x*y, list))
