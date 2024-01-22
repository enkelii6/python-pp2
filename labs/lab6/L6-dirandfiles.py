import os, string
path = os.getcwd()
# 1
print(f"Files: {[f for f in os.listdir(path) if os.path.isfile(f)]}, directories: {[d for d in os.listdir(path) if os.path.isdir(d)]} all elements are: {os.listdir(path)}")
# 2
print(f"Path accessibility: Existance: {os.access(path, mode=os.EX_OK)}, Reading: {os.access(path, mode=os.R_OK)}, Writing: {os.access(path, mode=os.W_OK)}, Executability: {os.access(path, mode=os.X_OK)}")
# 3
def checkUp(path):
    if os.access(path, mode=os.EX_OK):
        return os.listdir(path)
    else:
        return False
print(checkUp(path))
#4
with open('examplefile.txt', 'r') as file:
    x = sum(1 for line in file)
print(x)
#5
list = list(input().split())
with open('examplefile.txt', 'w') as file:
    for i in list:
        file.write(str(i) + ' ')
#6
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w'):
        pass
#7
with open('examplefile.txt', 'r') as r:
    with open('examplefile_copy.txt', 'w') as w:
        for line in r:
            w.write(line)
#8
with open('example2.txt', 'w') as w:
    if os.path.exists(path):
        w.write('')
