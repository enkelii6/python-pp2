# street address caeser encrypt from parsed file
import re, string
pattern1 = re.compile('^[a-zA-Z]+')
pattern2 = re.compile(', [0-9]+')
def encrypt(x):
    res = ''
    for i in x:
        if ord(i) != 122:
            res += chr(ord(i)+1)
        else:
            res += 'a'
    return res

with open('/Users/gleb/Desktop/pp2/python-pp2/adress.txt', 'r') as primary_file:
    needParse = primary_file.read()
    with open('adress_caeser.txt', 'w') as caeser_file:
        for line in needParse.splitlines():
            a = re.match(pattern1, line)
            b = re.search(pattern2, line)
            if a and b:
                caeser_file.write(encrypt(a.group()) + b.group() + '\n')
print(string.ascii_letters)
