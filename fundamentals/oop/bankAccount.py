# !/usr/bin/python3
from time import gmtime, strftime, localtime

class BankAccount:

    def __init__(self, int_rate= .005, balance= 0):
        self.balance = balance
        self.int_rate = int_rate
        self.record = [f'{BankAccount.get_time()}: Initial deposit ${str(balance)}']

    def deposit(self, amount):
        self.balance += amount
        self.record.append(f'{BankAccount.get_time()}: Deposit ${str(amount)}')
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.record.append(f'{BankAccount.get_time()}Withdrawl ${str(amount)}')
            return self
        print('Insufficient funds')
        self.record.append(f'{BankAccount.get_time()}: Withdrawl attempt for ${str(amount)}, insufficient funds')

        return self

    def display_account_info(self):
        print(f'Your balance is: ${self.balance}')
        print(f'Your interest rate is: {self.int_rate * 100}% \n ------------')
        return self

    def yield_interest(self):
        interest = self.balance * self.int_rate
        print(f'You have earned ${interest}')
        return self

    def history(self):
        record = self.record
        print(f'Account History:')
        for entry in self.record:
            print(f'{entry}')
        print(f'----------')

#static methods
    @staticmethod
    def get_time():
        accessTime = strftime('%d %b %Y %H:%M:%S', localtime())
        return accessTime


# begin execution
# 
# print(BankAccount.get_time())
# account1 = BankAccount(.005, 50)
# account2 = BankAccount(.015,1500)

# account1.deposit(56).deposit(92).deposit(25).withdraw(50).yield_interest().display_account_info()
# account1.history()

# account2.deposit(324).deposit(257).withdraw(50).withdraw(50).withdraw(500).withdraw(1000).yield_interest().display_account_info()
# account2.history()
