from collections import defaultdict


class ReportController:
    def __init__(self, transaction_controller):
        self.txn_ctrl = transaction_controller
