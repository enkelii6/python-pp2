def histogram(a):
    for i in range(len(a)):
        print(a[i]*'*')

histogram(list(map(int, input().split())))
