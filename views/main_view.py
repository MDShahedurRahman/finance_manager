class MainView:
    def show_accounts(self, accounts):
        print("Accounts:")
        for acc in accounts:
            print(f"{acc.account_id}: {acc.name} - Balance: {acc.balance}")
