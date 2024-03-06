import os
with open('labs/lab6/examplefile.txt', 'r') as r:
    with open('examplefile_copy.txt', 'w') as w:
        for line in r:
            w.write(line)
