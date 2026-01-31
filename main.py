def main():
    account_ctrl = AccountController()
    txn_ctrl = TransactionController(account_ctrl)
    report_ctrl = ReportController(txn_ctrl)
    main_view = MainView()
    report_view = ReportView()

    # Sample setup for commits
    acc1 = Account("acc1", "Checking", 1000)
    account_ctrl.add_account(acc1)
