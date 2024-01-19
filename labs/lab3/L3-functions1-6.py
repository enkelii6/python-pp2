sentence = list(input().split())
def rev(a):
    res = a[::-1]
    fin = ' '.join(map(str, res))
    print(fin)
rev(sentence)
