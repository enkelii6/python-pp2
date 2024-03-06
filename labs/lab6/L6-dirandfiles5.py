import os
list = list(input().split())
with open('labs/lab6/examplefile.txt', 'w') as file:
    for i in list:
        file.write(str(i) + ' ')
