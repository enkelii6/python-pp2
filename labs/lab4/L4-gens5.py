def ntozero(n):
    while n >= 0:
        yield n
        n -= 1

gen = ntozero(int(input()))
for value in gen:
    print(value)
