def solution(n):
    for i in range(n):
        if i%3 + i%4 == 0:
            yield i

gen = solution(int(input()))
for value in gen:
    print(value)
