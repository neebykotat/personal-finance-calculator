from finance import FinanceTracker

def main():
    tracker = FinanceTracker()
    print("Ваш трекер личных финансов")

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
            cat = input("Введите категорию дохода (например, Зарплата, Стипендия): ").strip()
            try:
                amt = float(input("Сумма: "))
                tracker.add_income(cat, amt)
                print(f"✅ Доход в категорию '{cat}' успешно добавлен!")
            except ValueError as e:
                print(f"❌ Ошибка: {e}")

        elif choice == "2":
            cat = input("Введите категорию расхода (например, Продукты, Фастфуд): ").strip()
            try:
                amt = float(input("Сумма: "))
                result_message = tracker.add_expense(cat, amt)
                print(result_message)
            except ValueError as e:
                print(f"❌ Ошибка: {e}")

        elif choice == "3":
            print(f"\n📈 Всего заработано: {tracker.get_total_income()} руб.")
            print(f"📉 Всего потрачено: {tracker.get_total_expense()} руб.")
            print(f"💳 Текущий баланс: {tracker.get_balance()} руб.")

        elif choice == "4":
            cat = input("Для какой категории установить лимит?: ").strip()
            try:
                amt = float(input("Введите сумму лимита: "))
                tracker.set_limit(cat, amt)
                print(f"🔒 Лимит для '{cat}' изменен на {amt} руб.")
            except ValueError as e:
                print(f"❌ Ошибка: {e}")

        elif choice == "5":
            print("👋 Программа завершена. Удачи в накоплениях!")
            break
        else:
            print("⚠️ Неверный пункт меню, попробуйте снова.")


if __name__ == "__main__":
    main()
