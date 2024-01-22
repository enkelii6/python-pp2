import re
pattern8 = re.compile('(?=[A-Z])')
print(re.split(pattern8, 'ILoveDana'))
