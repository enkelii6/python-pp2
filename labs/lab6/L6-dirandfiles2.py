import os
path = os.getcwd()
print(f"Path accessibility: Existance: {os.access(path, mode=os.EX_OK)}, Reading: {os.access(path, mode=os.R_OK)}, Writing: {os.access(path, mode=os.W_OK)}, Executability: {os.access(path, mode=os.X_OK)}")
