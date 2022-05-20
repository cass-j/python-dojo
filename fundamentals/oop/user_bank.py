# !/usr/bin/python3
from time import gmtime, strftime, localtime

# classes
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
            self.record.append(f'{BankAccount.get_time()}: Withdrawl ${str(amount)}')
            return self
        print('Insufficient funds')
        self.record.append(f'{BankAccount.get_time()}: Withdrawl attempt for ${str(amount)}, insufficient funds')

        return self

    def display_account_info(self):
        print(f'Your balance is: ${self.balance}')
        # print(f'Your interest rate is: {self.int_rate * 100}% \n ------------')
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

    @staticmethod
    def get_time():
        accessTime = strftime('%d %b %Y %H:%M:%S', localtime())
        return accessTime


class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = str.title(first_name)
        self.last_name = str.title(last_name)
        self.email = str.lower(email)
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate=0.02, balance=0)

    def display_info(self):
        print('----------')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        print(f'Reward Member Status: {self.is_rewards_member}')
        print(f'Gold card points:{self.gold_card_points}')
        return self

    def enroll(self):
        if self.is_rewards_member:
            print('----------')
            print('User already a member.')
            return self
        self.is_rewards_member = True
        print('----------')
        print('Enrollment successful')
        return self

    def add_points(self,amount):
        self.gold_card_points += amount
        return self

    def spend_points(self, amount):
        if self.is_rewards_member != True:
            print('----------')
            print('User is not a rewards member!')
            return self
        elif amount > self.gold_card_points:
            print('----------')
            print('User does not have required points!')
            return self

        print('----------')
        print(f'Purchase successful, {amount} points spent.')
        return self
    

# bankAccount Methods
    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def account_history(self):
        self.account.history()
        return self



#begin execution

smith = User('john', 'smith', 'john.smith@email.mail', 22)
smith.make_deposit(100)
smith.make_withdrawl(60)

smith.display_user_balance()
smith.account.history()