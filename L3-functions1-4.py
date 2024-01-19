lst = list(map(int, input().split()))
primes = filter(lambda x: all(x%i != 0 for i in range(2, x)), lst)
res = list(primes)
if 1 in res:
    res.remove(1)
print(res)
