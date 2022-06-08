from account import Account
import csv

class Owner:
    def __init__(self,owner_id,last_name,first_name,address,city,state):
        self.owner_id=owner_id
        self.last_name=last_name
        self.first_name=first_name
        self.address=address
        self.city=city
        self.state=state
        # self.account={}

    def all_owners():
        all_owners=[]
        with open("support/owners.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_owner = Owner(**row)
                all_owners.append(new_owner)
        return all_owners                     #not sure if we should make this an "init or class variable"

    def find_account(self):
        account_number=""
        # for owner in Owner.all_owners():
        # print(self.owner_id)
        with open("support/account_owners.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row["owner_id"])
                if row["owner_id"]==self.owner_id:
                    account_number=row["account_id"]
        for account in Account.all_accounts():
            if account.account_id==account_number:
                return account
                
    

Owner.all_owners()

# print(Owner.all_owners()[0].find_account())
Owner.all_owners()[0].find_account()
print(Owner.all_owners()[0].find_account().initial_balance)


# print(Owner.all_owners()[0].owner_id)


