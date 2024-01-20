def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

gen = even(int(input()))
for value in gen:
    print(value)
