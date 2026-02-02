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

    def add_transaction(self, transaction):
        account = self.account_controller.get_account(transaction.account_id)
        if not account:
            raise ValueError("Account not found")
        if transaction.category.type == "income":
            account.deposit(transaction.amount)
        else:
            account.withdraw(transaction.amount)
        self.transactions.append(transaction)
        self.save_transactions()
        self.account_controller.save_accounts()

    def list_transactions(self, account_id=None):
        if account_id:
            return [txn for txn in self.transactions if txn.account_id == account_id]
        return self.transactions

    def delete_transaction(self, txn_id):
        txn = next((t for t in self.transactions if t.txn_id == txn_id), None)
        if txn:
            account = self.account_controller.get_account(txn.account_id)
            if txn.category.type == "income":
                account.withdraw(txn.amount)
            else:
                account.deposit(txn.amount)
            self.transactions.remove(txn)
            self.save_transactions()
            self.account_controller.save_accounts()

    def update_transaction_amount(self, txn_id, new_amount):
        txn = next((t for t in self.transactions if t.txn_id == txn_id), None)
        if txn:
            account = self.account_controller.get_account(txn.account_id)
            if txn.category.type == "income":
                account.balance -= txn.amount
                account.balance += new_amount
            else:
                account.balance += txn.amount
                account.balance -= new_amount
            txn.amount = new_amount
            self.save_transactions()
            self.account_controller.save_accounts()
