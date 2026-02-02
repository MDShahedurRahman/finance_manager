class Category:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_  # "income" or "expense"

    def is_income(self):
        return self.type == "income"
