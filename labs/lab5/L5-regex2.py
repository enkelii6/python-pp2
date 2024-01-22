import re
pattern2 = re.compile("^[a]{1}[b]{2,3}$")
print(pattern2.search("abbb"))
