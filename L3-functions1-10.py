def unique(a):
    res = []
    for i in a:
        if i not in res:
            res.append(i)
    return res

print(unique([1, 2, 1, 1, 2, 2]))
