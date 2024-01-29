from itertools import permutations
def perm(a):
    res = permutations(a)
    for i in res:
        print(''.join(i))

perm('ab')
