import json
from models.account import Account
from config import ACCOUNTS_FILE


class AccountController:
    def __init__(self):
        self.accounts = self.load_accounts()
