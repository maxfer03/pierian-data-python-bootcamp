class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        # print('Account owner:  ', self.owner)
        # print('Account balance:', self.balance)

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, amount):
        self.balance += amount
        return 'Deposit Accepted'
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            return f"Withdrawal Denied. Can't withdraw more cash than {self.balance}"
        else:
            self.balance -= amount
            return 'Withdrawal Accepted'




acct1 = Account("Max", 1000)

print(acct1)

print(acct1.balance)

print(acct1.deposit(100))

print(acct1.balance)

print(acct1.withdraw(100))

print(acct1.balance)

print(acct1.withdraw(1100))

print(acct1.balance)



