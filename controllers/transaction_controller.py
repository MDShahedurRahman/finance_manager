import json
from models.transaction import Transaction
from config import TRANSACTIONS_FILE
from controllers.account_controller import AccountController


class TransactionController:
    def __init__(self, account_controller):
        self.account_controller = account_controller
        self.transactions = self.load_transactions()


def load_transactions(self):
    try:
        with open(TRANSACTIONS_FILE, "r") as f:
            data = json.load(f)
            return [Transaction(**txn) for txn in data]
    except FileNotFoundError:
        return []


def save_transactions(self):
    with open(TRANSACTIONS_FILE, "w") as f:
        json.dump([txn.__dict__ for txn in self.transactions], f, indent=2)
