def spy_game(a):
    for i in range(len(a) - 2):
        if a[i] == a[i+1] and a[i] == 0 and a[i+2] == 7:
            return True
        else:
            continue
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,7,2,0,4,5,0]))
