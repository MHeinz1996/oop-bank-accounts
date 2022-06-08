
import csv
import datetime
class Account:
    def __init__(self,account_id, initial_balance, open_date):
        self.account_id=account_id
        self.initial_balance=round(((int(initial_balance))/100),2)
        self.open_date=open_date
        if (self.initial_balance) < 0:
            raise Exception("Sorry, no numbers below zero")
        self.balance=round(((int(initial_balance))/100),2)



    def withdraw(self,amount):
        self.balance-= amount
        if self.balance-amount<0:
            raise Exception ("Sorry, you do not have enough to withdraw that amount.")
        return self.balance

    def deposit(self,amount):
        self.balance+= amount
        return self.balance

    # def get_owner(self,name,address,phone):
    #     self.owner=Owner(name,address,phone)
    @staticmethod
    def all_accounts():
        all_accounts=[]
        with open("support/accounts.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_account = Account(**row)
                all_accounts.append(new_account)
        return all_accounts                     #not sure if we should make this an "init or class variable"

    def find_id(account_id):        #should we have made this a self? seems weird that every account instance would have access to ALL accounts??
        for account in Account.all_accounts():
            if account.account_id==account_id:
                return account



# account_one=Account(1234,50)
# account_one.get_owner("John Baker", "1124 Sesame St. Boise,ID 83704", "555-208-1234")
# print(account_one.owner.name)
# print(account_one.all_accounts()[0].ID)

# Account.all_accounts()
Account.all_accounts()[0].account_id
# print(Account.find_id("1212").initial_balance)

print(type(Account.all_accounts()[0].account_id))
