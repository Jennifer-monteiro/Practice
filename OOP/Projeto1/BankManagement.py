""" Bank Account Management:
Develop a BankAccount class with attributes such as account number, 
balance, and owner's name. 
Implement methods to deposit, withdraw, and check balance. """

class BankAccount:
    def __init__(self, account,balance, name):
        self.account = account
        self.balance = balance
        self.name = name

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "INSUFICIENT FUNDS"
        
    def check_balance(self):
        return self.balance
    
bank_info1 = BankAccount(256445,1000,"Jen")
bank_info2 = BankAccount(256415,1000,"aaa")
bank_info3 = BankAccount(256465,1000,"bbb")

bank_info1.deposit(50)
print(bank_info1.check_balance())
print(bank_info2.check_balance())

# Test deposit method
print("Initial balances:")
print("Bank info 1:", bank_info1.check_balance())
print("Bank info 2:", bank_info2.check_balance())
print("Bank info 3:", bank_info3.check_balance())

bank_info1.deposit(200)
bank_info2.deposit(300)
bank_info3.deposit(400)

print("\nBalances after deposit:")
print("Bank info 1:", bank_info1.check_balance())
print("Bank info 2:", bank_info2.check_balance())
print("Bank info 3:", bank_info3.check_balance())

# Test withdraw method
print("\nBalances before withdrawal:")
print("Bank info 1:", bank_info1.check_balance())
print("Bank info 2:", bank_info2.check_balance())
print("Bank info 3:", bank_info3.check_balance())

bank_info1.withdraw(100)
bank_info2.withdraw(200)
bank_info3.withdraw(300)

print("\nBalances after withdrawal:")
print("Bank info 1:", bank_info1.check_balance())
print("Bank info 2:", bank_info2.check_balance())
print("Bank info 3:", bank_info3.check_balance())