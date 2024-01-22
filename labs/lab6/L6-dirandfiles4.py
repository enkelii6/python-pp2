import os
with open('examplefile.txt', 'r') as file:
    x = sum(1 for line in file)
print(x)
