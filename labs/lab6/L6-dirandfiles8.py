import os
with open('example2.txt', 'w') as w:
    if os.path.exists('example2.txt'):
        w.write('')
