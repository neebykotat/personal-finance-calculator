from finance import FinanceTracker


def main():
    tracker = FinanceTracker()
    print("Ваш трекер личных финансов v2.0")

    tracker.set_limit("Фастфуд", 1500)
    print("* Установлен тестовый лимит на категорию 'Фастфуд': 1500 руб.")

    while True:
        print("\n--- МЕНЮ ---")
        print("1. ➕ Добавить доход")
        print("2. ➖ Добавить расход")
        print("3. 📊 Показать баланс и статистику")
        print("4. ⚙️ Установить лимит на категорию")
        print("5. 🚪 Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            msg = "Введите категорию дохода (например, Зарплата, Стипендия): "
            cat = input(msg).strip()
            try:
                amt = float(input("Сумма: "))
                tracker.add_income(cat, amt)
                print("✅ Доход в категорию '{}' успешно добавлен!".format(cat))
            except ValueError as e:
                print("❌ Ошибка: {}".format(e))

        elif choice == "2":
            msg = "Введите категорию расхода (например, Продукты, Фастфуд): "
            cat = input(msg).strip()
            try:
                amt = float(input("Сумма: "))
                result_message = tracker.add_expense(cat, amt)
                print(result_message)
            except ValueError as e:
                print("❌ Ошибка: {}".format(e))

        elif choice == "3":
            print("\n📈 Всего заработано: {} руб.".format(
                tracker.get_total_income()
            ))
            print("📉 Всего потрачено: {} руб.".format(
                tracker.get_total_expense()
            ))
            print("💳 Текущий баланс: {} руб.".format(
                tracker.get_balance()
            ))

        elif choice == "4":
            cat = input("Для какой категории установить лимит?: ").strip()
            try:
                amt = float(input("Введите сумму лимита: "))
                tracker.set_limit(cat, amt)
                print("🔒 Лимит для '{}' изменен на {} руб.".format(cat, amt))
            except ValueError as e:
                print("❌ Ошибка: {}".format(e))

        elif choice == "5":
            print("👋 Программа завершена. Удачи в накоплениях!")
            break
        else:
            print("⚠️ Неверный пункт меню, попробуйте снова.")


if __name__ == "__main__":
    main()
