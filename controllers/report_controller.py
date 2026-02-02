from collections import defaultdict


class ReportController:
    def __init__(self, transaction_controller):
        self.txn_ctrl = transaction_controller

    def total_income(self):
        return sum(txn.amount for txn in self.txn_ctrl.transactions if txn.category.type == "income")

    def total_expense(self):
        return sum(txn.amount for txn in self.txn_ctrl.transactions if txn.category.type == "expense")

    def balance_by_category(self):
        report = defaultdict(float)
        for txn in self.txn_ctrl.transactions:
            report[txn.category.name] += txn.amount if txn.category.type == "income" else -txn.amount
        return report

    def expense_by_category(self):
        report = {}
        for txn in self.txn_ctrl.transactions:
            if txn.category.type == "expense":
                report[txn.category.name] = report.get(
                    txn.category.name, 0) + txn.amount
        return report

    def income_by_category(self):
        report = {}
        for txn in self.txn_ctrl.transactions:
            if txn.category.type == "income":
                report[txn.category.name] = report.get(
                    txn.category.name, 0) + txn.amount
        return report

    def net_balance(self):
        return self.total_income() - self.total_expense()
