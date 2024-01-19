class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, monthes):
        for i in range(monthes):
            self.balance += 0.1*self.balance
        print("Now you have", self.balance)
    def withdraw(self, money):
        if money<0:
            print("How you want to withdraw negative amount of money???")
        elif money>self.balance:
            print("Not enough balance")
        else:
            print("Take Your Money, Sir")
            self.balance -= money
    def show(self):
        print("You have", self.balance)

x = Account("Ilya Kuleshov", 5)
x.deposit(12)
x.withdraw(1000)
x.withdraw(-100)
x.withdraw(5)
x.show()
