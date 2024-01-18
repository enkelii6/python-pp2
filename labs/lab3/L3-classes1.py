"""
class String:
    def __init__(self, string):
        self.string = string

    def print_str(self):
        print(self.string)

print("Type a text you want:")
x = String(str(input()))
x.print_str()
"""

class String:
    def get_str(self):
        self.content = str(input())

    def print_str(self):
        print(self.content)

x = String()
print("Enter String:")
x.get_str()
x.print_str()