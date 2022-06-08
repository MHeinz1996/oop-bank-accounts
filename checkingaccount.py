from account import Account

class Checking_Account(Account):

    def __init__(self,account_id, initial_balance, open_date):
        super().__init__(account_id, initial_balance, open_date)
        self.initial_balance=round((int(initial_balance)),2)
        self.check_withdrawls=0
        self.balance=round((int(initial_balance)),2)

    def withdraw(self,amount):
        self.balance-= (amount+1)
        if self.balance-amount<0:
            raise Exception ("Sorry, you cannot overdraft your account!")
        return self.balance

    def withdraw_using_check(self,amount):
        # print(self.balance)
        if self.check_withdrawls>=3:
            self.balance-= (amount+2)
        else: 
            self.balance-= (amount)
        if self.balance-amount < -10:
            raise Exception ("Sorry, you cannot overdraft your account more than $10!")
        self.check_withdrawls+=1

        return self.balance
    
    def reset_checks(self):
        self.check_withdrawls=0


account_three=Checking_Account("555",3000,"6/5/22")

print(account_three.balance)

account_three.withdraw_using_check(100)
account_three.withdraw_using_check(100)
account_three.withdraw_using_check(100)
account_three.withdraw_using_check(100)
# account_three.withdraw_using_check(3011)
print(account_three.balance)
account_three.reset_checks()
account_three.withdraw_using_check(100)
print(account_three.balance)

