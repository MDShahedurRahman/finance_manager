from collections import defaultdict


class ReportController:
    def __init__(self, transaction_controller):
        self.txn_ctrl = transaction_controller


def total_income(self):
    return sum(txn.amount for txn in self.txn_ctrl.transactions if txn.category.type == "income")


def total_expense(self):
    return sum(txn.amount for txn in self.txn_ctrl.transactions if txn.category.type == "expense")
