from account import Account
from owner import Owner

class Bank:
    def __init__(self):
        self.bank_accounts=Account.all_accounts()
        self.bank_account_owners=Owner.all_owners()

    def find_account(self, owner_id):
        return Owner.find_account(owner_id)


