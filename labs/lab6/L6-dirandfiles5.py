import os
list = list(input().split())
with open('examplefile.txt', 'w') as file:
    for i in list:
        file.write(str(i) + ' ')
