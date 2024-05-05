import sys
from storage import load_transactions, save_transactions
from finance_manager import add_transaction, edit_transaction, search_transactions, calculate_balance


def print_menu():
    """
    Выводит на экран основное меню приложения.
    """
    print("\nДобро пожаловать в личный финансовый кошелек!")
    print("1. Показать баланс")
    print("2. Добавить транзакцию")
    print("3. Редактировать транзакцию")
    print("4. Поиск транзакций")
    print("5. Выход")


def handle_add_transaction(transactions):
    """
    Обрабатывает добавление новой транзакции.
    """
    date = input("Введите дату (ГГГГ-ММ-ДД): ")
    category = input("Введите категорию (Доход/Расход): ")
    amount = input("Введите сумму: ")
    description = input("Введите описание: ")
    new_transaction = {'Дата': date, 'Категория': category, 'Сумма': amount, 'Описание': description}
    add_transaction(transactions, new_transaction)
    save_transactions('data/transactions.csv', transactions)
    print("Транзакция добавлена.")


def handle_edit_transaction(transactions):
    """
    Обрабатывает редактирование существующей транзакции.
    """
    transaction_index = int(input("Введите номер транзакции для редактирования: ")) - 1
    if 0 <= transaction_index < len(transactions):
        date = input("Введите новую дату (ГГГГ-ММ-ДД): ")
        category = input("Введите новую категорию (Доход/Расход): ")
        amount = input("Введите новую сумму: ")
        description = input("Введите новое описание: ")
        updated_transaction = {'Дата': date, 'Категория': category, 'Сумма': amount, 'Описание': description}
        edit_transaction(transactions, transaction_index, updated_transaction)
        save_transactions('data/transactions.csv', transactions)
        print("Транзакция обновлена.")
    else:
        print("Неверный номер транзакции.")


def main():
    transactions = load_transactions('data/transactions.csv')
    while True:
        print_menu()
        choice = input("Выберите действие: ")
        if choice == '1':
            balance = calculate_balance(transactions)
            print(f"Баланс: {balance['Баланс']}, Доходы: {balance['Доходы']}, Расходы: {balance['Расходы']}")
        elif choice == '2':
            handle_add_transaction(transactions)
        elif choice == '3':
            handle_edit_transaction(transactions)
        elif choice == '4':
            category = input("Введите категорию для поиска: ")
            date = input("Введите дату для поиска: ")
            amount = input("Введите сумму для поиска: ")
            found_transactions = search_transactions(transactions, category, date, int(amount) if amount else None)
            for t in found_transactions:
                print(t)
        elif choice == '5':
            print("Выход из программы.")
            sys.exit(0)
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
