from datetime import datetime


class Transaction:
    def __init__(self, txn_id, account_id, category, amount, date=None, description=""):
        self.txn_id = txn_id
        self.account_id = account_id
        self.category = category
        self.amount = amount
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.description = description
