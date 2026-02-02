import json
from models.account import Account
from config import ACCOUNTS_FILE


class AccountController:
    def __init__(self):
        self.accounts = self.load_accounts()

    def load_accounts(self):
        try:
            with open(ACCOUNTS_FILE, "r") as f:
                data = json.load(f)
                return [Account(**acc) for acc in data]
        except FileNotFoundError:
            return []

    def save_accounts(self):
        with open(ACCOUNTS_FILE, "w") as f:
            json.dump([acc.__dict__ for acc in self.accounts], f, indent=2)

    def add_account(self, account):
        self.accounts.append(account)
        self.save_accounts()

    def get_account(self, account_id):
        for acc in self.accounts:
            if acc.account_id == account_id:
                return acc
        return None

    def delete_account(self, account_id):
        self.accounts = [
            acc for acc in self.accounts if acc.account_id != account_id]
        self.save_accounts()

    def update_account_name(self, account_id, new_name):
        acc = self.get_account(account_id)
        if acc:
            acc.name = new_name
            self.save_accounts()
