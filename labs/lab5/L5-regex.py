import re

pattern1 = re.compile("^[a]{1}[b]+$")
print(pattern1.search("abb"))

pattern2 = re.compile("^[a]{1}[b]{2,3}$")
print(pattern2.search("abbb"))

pattern3 = re.compile("[a-z]+[_]{1}")
print(pattern3.search("GFHBJKLUYTaoiinfsdj_hjcjkas"))

pattern4 = re.compile("[A-Z]{1}[a-z]+")
print(pattern4.search("Gleb"))

pattern5 = re.compile("^[a]{1}.+[b]{1}$")
print(pattern5.search("aTYGJBHKIK&*^%^YTb"))

string = 'i.love,Dana '
print(string.replace(' ', ':').replace('.', ':').replace(',', ':'))

def snake_to_camel(snake):
    return re.sub('_(.)', lambda x: x.group(1).upper(), snake)
print(snake_to_camel('i_love_dana'))

pattern8 = re.compile('(?=[A-Z])')
print(re.split(pattern8, 'ILoveDana'))

print(pattern8.sub(' ', 'ILoveDana'))

def camelToSnake(camel):
    almCamel = pattern8.sub('_', camel)
    return almCamel.lower()
print(camelToSnake('iLoveDana'))
