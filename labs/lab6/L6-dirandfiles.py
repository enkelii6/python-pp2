import os
path = os.getcwd()
print(f"Files: {[f for f in os.listdir(path) if os.path.isfile(f)]}, directories: {[d for d in os.listdir(path) if os.path.isdir(d)]} all elements are: {os.listdir(path)}")
