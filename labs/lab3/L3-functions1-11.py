def palindrome(x):
    return x == x[::-1]
if palindrome(input()):
    print(True)
else:
    print(False)
