class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = self.calculate_expenses()

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):
        total_expenses = 0
        for items in args:
            for item in items:
                if type(item).__name__ != "Child":
                    total_expenses += item.get_monthly_expense()
                else:
                    total_expenses += item.cost * 30

        return total_expenses
