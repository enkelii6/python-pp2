import re
pattern = re.compile('(?=[A-Z])')
print(pattern.sub(' ', 'ILoveDana'))
