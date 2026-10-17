class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.category_limits = {}

    def set_limit(self, category: str, limit: float):
        if limit < 0:
            raise ValueError("Лимит не может быть отрицательным")
        self.category_limits[category] = limit

    def add_income(self, category: str, amount: float):
        if amount <= 0:
            raise ValueError("Сумма дохода должна быть больше нуля")
        self.transactions.append({
            'type': 'income',
            'category': category,
            'amount': amount
        })

    def add_expense(self, category: str, amount: float):
        if amount <= 0:
            raise ValueError("Сумма расходов должна быть больше нуля")

        self.transactions.append({
            'type': 'expense',
            'category': category,
            'amount': amount
        })

        current_category_spent = sum(
            t['amount'] for t in self.transactions
            if t['type'] == 'expense' and t['category'] == category
        )

        if (category in self.category_limits and
                current_category_spent > self.category_limits[category]):
            return "⚠️ Внимание! Превышен лимит по категории '{}'!".format(
                category
            )
        return "✅ Расход успешно добавлен"

    def get_total_income(self) -> float:
        return sum(
            t['amount'] for t in self.transactions if t['type'] == 'income'
        )

    def get_total_expense(self) -> float:
        return sum(
            t['amount'] for t in self.transactions if t['type'] == 'expense'
        )

    def get_balance(self) -> float:
        return self.get_total_income() - self.get_total_expense()

    def get_history_by_type(self, op_type: str) -> list:
        if op_type not in ['income', 'expense']:
            raise ValueError("Тип операции должен быть 'income' или 'expense'")
        return [t for t in self.transactions if t['type'] == op_type]