import sys

from finance_manager import add_transaction, edit_transaction, search_transactions, calculate_balance, \
    list_transactions, clear_transactions
from storage import load_transactions, save_transactions

transactions = []


def print_transaction(transaction):
    """
    Печатает транзакцию в форматированном виде.
    """
    print(f"\nДата: {transaction['Дата']}")
    print(f"Категория: {transaction['Категория']}")
    print(f"Сумма: {transaction['Сумма']}")
    print(f"Описание: {transaction['Описание']}\n")


def print_menu():
    print("\nДобро пожаловать в личный финансовый кошелек!")
    print("1. Показать баланс")
    print("2. Добавить транзакцию")
    print("3. Редактировать транзакцию")
    print("4. Поиск транзакций")
    print("5. Просмотреть все транзакции")
    print("6. Очистить все транзакции")
    print("7. Выход")


def handle_add_transaction(trans_add):
    """
    Запрашивает данные у пользователя и добавляет новую транзакцию.
    """
    date = input("Введите дату (ГГГГ-ММ-ДД): ")
    print("Выберите категорию:\n 1. Доход\n 2. Расход")
    category_choice = input("Ваш выбор (1 или 2): ")
    category = 'Доход' if category_choice == '1' else 'Расход'
    amount = input("Введите сумму: ")
    description = input("Введите описание: ")
    new_transaction = {'Дата': date, 'Категория': category, 'Сумма': amount, 'Описание': description}
    trans_add = add_transaction(trans_add, new_transaction)
    save_transactions('data/transactions.csv', trans_add)
    print("Транзакция добавлена.")


def handle_edit_transaction(trans_edit):
    """
    Обрабатывает редактирование существующей транзакции.
    """
    transaction_index = int(input("Введите номер транзакции для редактирования: ")) - 1
    if 0 <= transaction_index < len(trans_edit):
        date = input("Введите новую дату (ГГГГ-ММ-ДД): ")
        category = input("Введите новую категорию (Доход/Расход): ")
        amount = input("Введите новую сумму: ")
        description = input("Введите новое описание: ")
        updated_transaction = {'Дата': date, 'Категория': category, 'Сумма': amount, 'Описание': description}
        edit_transaction(trans_edit, transaction_index, updated_transaction)
        save_transactions('data/transactions.csv', trans_edit)
        print("Транзакция обновлена.")
    else:
        print("Неверный номер транзакции.")


def handle_list_transactions(trans_list):
    """
    Обрабатывает вывод всех транзакций.
    """
    print("\nСписок всех транзакций:")
    transactions_info = list_transactions(trans_list)
    print(transactions_info)


def handle_clear_transactions():
    """
    Удаляет все транзакции и сохраняет изменения в файл.
    """
    global transactions  # Используем глобальную переменную, если она введена
    transactions = clear_transactions()  # Очищаем транзакции
    save_transactions('data/transactions.csv', transactions)  # Сохраняем пустой список в файл
    print("Все транзакции были успешно удалены.")


def handle_search_transactions():
    """
    Обрабатывает поиск транзакций по категории, дате и сумме.
    """
    print("Введите критерии поиска:")
    category = input("Категория (оставьте пустым, если не требуется): ")
    date = input("Дата (ГГГГ-ММ-ДД, оставьте пустым, если не требуется): ")
    amount_input = input("Сумма (оставьте пустым, если не требуется): ")
    amount = int(amount_input) if amount_input else None

    found_transactions = search_transactions(transactions, category if category else None, date if date else None,
                                             amount)
    if found_transactions:
        print("\nНайденные транзакции:")
        for transaction in found_transactions:
            print_transaction(transaction)
    else:
        print("Транзакции не найдены.")


def main():
    global transactions
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
            handle_search_transactions()
        elif choice == '5':
            handle_list_transactions(transactions)
        elif choice == '6':
            handle_clear_transactions()
        elif choice == '7':
            print("Выход из программы.")
            sys.exit(0)
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
