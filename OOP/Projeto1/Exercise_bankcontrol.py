""" Bank Account Management:
Create a class named BankAccount. It should have attributes balance and owner, 
and methods to deposit, withdraw, and check the balance. """

class BankAccount:

    def __init__(self,balance,owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        return self.balance 

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"
    
    def check_balance(self):
        return self.balance
    
    def __str__(self):
        return f"{self.owner}, o seu saldo é de: {self.balance}"
    
account = BankAccount(1000, "John")
account.deposit(500)
print(account.check_balance())
account.withdraw(200)
print(account.check_balance())

print(account)
