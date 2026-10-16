import pytest
from finance import FinanceTracker

def test_add_income_and_balance():
    """Тест на правильное суммирование доходов -> увеличение баланса"""
    tracker = FinanceTracker()
    tracker.add_income("Зарплата", 50000)
    tracker.add_income("Стипендия", 5000)
    assert tracker.get_total_income() == 55000
    assert tracker.get_balance() == 55000


def test_invalid_operations_raise_errors():
    """Тест ввода отрицательных / нулевых сумм"""
    tracker = FinanceTracker()
    with pytest.raises(ValueError):
        tracker.add_income("Инвестиции", -100)
    with pytest.raises(ValueError):
        tracker.add_expense("Такси", 0)


def test_category_limit_warning():
    """Тест уведомлений о превышении лимита"""
    tracker = FinanceTracker()
    tracker.set_limit("Кафе", 2000)

    # Всё норм
    status1 = tracker.add_expense("Кафе", 1200)
    assert "успешно добавлен" in status1

    # Превышение
    status2 = tracker.add_expense("Кафе", 900)
    assert "Превышен лимит" in status2


def test_history_filtering():
    """Тест фильтра истории"""
    tracker = FinanceTracker()
    tracker.add_income("Зарплата", 1000)
    tracker.add_expense("Метро", 50)

    incomes = tracker.get_history_by_type('income')
    expenses = tracker.get_history_by_type('expense')

    assert len(incomes) == 1
    assert len(expenses) == 1
    assert incomes[0]['category'] == "Зарплата"
    assert expenses[0]['category'] == "Метро"
