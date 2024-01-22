import os
path = os.getcwd()
def checkUp(path):
    if os.access(path, mode=os.EX_OK):
        return os.listdir(path)
    else:
        return False
print(checkUp(path))
