import re
pattern = re.compile('(?=[A-Z])')
def camelToSnake(camel):
    almCamel = pattern.sub('_', camel)
    return almCamel.lower()
print(camelToSnake('iLoveDana'))
