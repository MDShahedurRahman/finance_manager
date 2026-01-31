import json
from models.transaction import Transaction
from config import TRANSACTIONS_FILE
from controllers.account_controller import AccountController


class TransactionController:
    def __init__(self, account_controller):
        self.account_controller = account_controller
        self.transactions = self.load_transactions()
