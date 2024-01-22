import re
def snake_to_camel(snake):
    return re.sub('_(.)', lambda x: x.group(1).upper(), snake)
print(snake_to_camel('i_love_dana'))
