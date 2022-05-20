# !/usr/bin/python3
import bankAccount

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


smith = User('john', 'smith', 'john.smith@email.mail', 22)
# smith.display_info().enroll().add_points(100)

# jones = User('james', 'jones', 'james.jones@email.mail', 57)
# brown = User('john', 'brown', 'john.brown@email.mail', 34)

# smith.spend_points(50)

# jones.enroll().spend_points(80)

# smith.display_info()
# jones.display_info()
# brown.display_info()

# smith.enroll()

# brown.spend_points(40)