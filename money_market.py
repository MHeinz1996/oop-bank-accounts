from account import Account

class Money_Market(Account):
    def __init__(self,account_id, initial_balance, open_date):
        super().__init__(account_id, initial_balance, open_date)
        self.initial_balance=round((int(initial_balance)),2)
        self.balance=round((int(initial_balance)),2)
        if (self.initial_balance) < 10000:
            raise Exception("Sorry, you need $10,000 to open this account")
        self.transactions=0

    def withdraw(self,amount):
        if self.transactions <6:
            self.balance-= amount
            self.transactions+=1
            if self.balance<10000:
                self.transactions=6
                self.balance-=100
                print("You have incurred a $100 fee for not maintaining a minimum of $10,000 in your account. You will not be able to withdraw more money until your balance is above $10,000.")
        else:
            print("Sorry, you have already hit your limit of 6 transactions per month")
        return self.balance

    def deposit(self,amount):
        if self.transactions <6:
            if self.balance <10000 and self.balance+amount >= 10000:
                self.balance+= amount
            else:
                self.balance+= amount
                self.transactions+=1
        elif self.transactions>=6:
            if self.balance <10000 and self.balance+amount >= 10000:
                self.balance+= amount
            else:
                print("Sorry, you have already hit your limit of 6 transactions per month")
        
        return self.balance