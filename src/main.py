import sys

from finance_manager import add_transaction, edit_transaction, calculate_balance, list_transactions
from storage import load_transactions, save_transactions


def print_menu():
    print("\nДобро пожаловать в личный финансовый кошелек!")
    print("1. Показать баланс")
    print("2. Добавить транзакцию")
    print("3. Редактировать транзакцию")
    print("4. Поиск транзакций")
    print("5. Просмотреть все транзакции")
    print("6. Выход")


def handle_add_transaction(transactions):
    """
    Запрашивает данные у пользователя и добавляет новую транзакцию.
    """
    date = input("Введите дату (ГГГГ-ММ-ДД): ")
    category = input("Введите категорию (Доход/Расход): ")
    amount = input("Введите сумму: ")
    description = input("Введите описание: ")
    new_transaction = {'Дата': date, 'Категория': category, 'Сумма': amount, 'Описание': description}
    transactions = add_transaction(transactions, new_transaction)
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


def handle_list_transactions(transactions):
    """
    Обрабатывает вывод всех транзакций.
    """
    print("\nСписок всех транзакций:")
    print(list_transactions(transactions))


def handle_search_transactions(transactions):
    pass


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
            handle_search_transactions(transactions)
        elif choice == '5':
            handle_list_transactions(transactions)
        elif choice == '6':
            print("Выход из программы.")
            sys.exit(0)
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
