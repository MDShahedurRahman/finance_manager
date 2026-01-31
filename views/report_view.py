class ReportView:
    def display_summary(self, income, expense, balance_by_category):
        print(f"Total Income: {income}")
        print(f"Total Expense: {expense}")
        print("Balance by Category:")
        for cat, amt in balance_by_category.items():
            print(f"{cat}: {amt}")
