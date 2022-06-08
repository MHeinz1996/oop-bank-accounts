from argparse import ArgumentError
from account import Account

class Savings_Account(Account):
    def __init__(self,account_id, initial_balance, open_date):
        super().__init__(account_id, initial_balance, open_date)
        self.initial_balance=round((int(initial_balance)),2)
        if (self.initial_balance) < 10:
            raise ValueError("Sorry, no numbers below ten")  #argument error?
        self.balance=round((int(initial_balance)),2)

    def withdraw(self,amount):
        self.balance-= (amount+2)
        if self.balance-amount<10:
            raise Exception ("Sorry, you must maintain a minimum balance of $10.")
        return self.balance

    def add_interest(self,rate):
        interest=round(((self.balance*rate)/100),2)
        self.balance+=interest
        return f"${interest}"

account_one=Savings_Account("555","3000","6/5/22")
print(account_one.withdraw(5))
print(account_one.add_interest(.08))





