import os
with open('examplefile.txt', 'r') as r:
    with open('examplefile_copy.txt', 'w') as w:
        for line in r:
            w.write(line)
