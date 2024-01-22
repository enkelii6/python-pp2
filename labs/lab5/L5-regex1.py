import re
pattern1 = re.compile("^[a]{1}[b]+$")
print(pattern1.search("abb"))
