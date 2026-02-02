class ReportView:
    def display_summary(self, income, expense, balance_by_category):
        print(f"Total Income: {income}")
        print(f"Total Expense: {expense}")
        print("Balance by Category:")
        for cat, amt in balance_by_category.items():
            print(f"{cat}: {amt}")

    def display_income_by_category(self, report):
        print("Income by Category:")
        for cat, amt in report.items():
            print(f"{cat}: {amt}")

    def display_expense_by_category(self, report):
        print("Expense by Category:")
        for cat, amt in report.items():
            print(f"{cat}: {amt}")
