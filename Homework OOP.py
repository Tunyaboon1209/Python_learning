class ATM():
    def __init__(self, accountname, balance):
        self.accountname = accountname
        self.balance = balance
    def __str__(self):
        text = f"User name: {self.accountname} | Curent balance = {self.balance}"
        return text
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def checkBalance(self):
        print(f"Total balance: {self.balance}")

user1 = ATM("Team", 1000)
user1.deposit(200)
print(user1)
user1.withdraw(500)
print(user1)
user1.checkBalance()