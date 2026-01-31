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
