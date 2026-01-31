class MainView:
    def show_accounts(self, accounts):
        print("Accounts:")
        for acc in accounts:
            print(f"{acc.account_id}: {acc.name} - Balance: {acc.balance}")

    def show_transactions(self, transactions):
        print("Transactions:")
        for txn in transactions:
            print(
                f"{txn.txn_id}: {txn.account_id} | {txn.category.name} | {txn.amount} | {txn.date} | {txn.description}")
