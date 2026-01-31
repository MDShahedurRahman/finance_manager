from controllers.account_controller import AccountController
from controllers.transaction_controller import TransactionController
from controllers.report_controller import ReportController
from models.account import Account
from models.transaction import Transaction
from models.category import Category
from views.main_view import MainView
from views.report_view import ReportView


def main():
    account_ctrl = AccountController()
    txn_ctrl = TransactionController(account_ctrl)
    report_ctrl = ReportController(txn_ctrl)
    main_view = MainView()
    report_view = ReportView()

    # Sample setup for commits
    acc1 = Account("acc1", "Checking", 1000)
    acc2 = Account("acc2", "Savings", 5000)
    account_ctrl.add_account(acc1)
    account_ctrl.add_account(acc2)

    cat_income = Category("Salary", "income")
    cat_expense = Category("Groceries", "expense")
    txn1 = Transaction("txn1", "acc1", cat_income, 2000,
                       description="Monthly Salary")
    txn2 = Transaction("txn2", "acc1", cat_expense, 150,
                       description="Grocery shopping")
    txn_ctrl.add_transaction(txn1)
    txn_ctrl.add_transaction(txn2)

    main_view.show_accounts(account_ctrl.accounts)
    main_view.show_transactions(txn_ctrl.transactions)

    income = report_ctrl.total_income()
    expense = report_ctrl.total_expense()
    balance_cat = report_ctrl.balance_by_category()
    report_view.display_summary(income, expense, balance_cat)
