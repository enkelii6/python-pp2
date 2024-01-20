def squares(a, b):
    for i in range(a, b+1):
        yield i**2
gen = squares(int(input()), int(input()))
for value in gen:
    print(value)
