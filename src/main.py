import sys
import time

from _datetime import datetime
from typing import List, Dict, Optional
from finance_manager import add_transaction, edit_transaction, search_transactions, calculate_balance, \
    list_transactions, clear_transactions
from storage import load_transactions, save_transactions

transactions = []


def print_menu():
    """
    Печатает меню выбора команд в терминале
    """
    print("\nДобро пожаловать в личный финансовый кошелек!")
    print("1. Показать баланс")
    print("2. Добавить транзакцию")
    print("3. Редактировать транзакцию")
    print("4. Поиск транзакций")
    print("5. Просмотреть все транзакции")
    print("6. Очистить все транзакции")
    print("7. Выход")


def print_transaction(transaction: Dict[str, str]) -> None:
    """
    Печатает транзакцию в форматированном виде.
    """
    amount = int(transaction['Сумма'])  # Преобразуем строку в число для безопасного форматирования
    print(f"\nДата: {transaction['Дата']}")
    print(f"Категория: {transaction['Категория']}")
    print(f"Сумма: {amount:,}")  # Форматирование суммы с разделителями тысяч
    print(f"Описание: {transaction['Описание']}\n")


def validate_date(date_str: str) -> Optional[str]:
    """
    Проверяет, что введенная дата корректна и соответствует формату ГГГГ-ММ-ДД.

    :param date_str: Строка с датой
    :return: Строка с датой или None, если дата невалидна
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("Некорректный формат даты. Пожалуйста, используйте формат ГГГГ-ММ-ДД.")
        return None


def validate_amount(amount_str: str) -> Optional[str]:
    """
    Проверяет, что введенная сумма корректна и является числом.

    :param amount_str: Строка с суммой
    :return: Сумма в виде строки без разделителей или None, если сумма невалидна
    """
    try:
        # Удаляем запятые для поддержки разделителей тысяч
        clean_amount_str = amount_str.replace(',', '')
        # Преобразуем в число для проверки
        amount = int(clean_amount_str)
        return str(amount)  # Возвращаем строковое представление для единообразия
    except ValueError:
        print("Некорректная сумма. Введите число.")
        return None


def handle_add_transaction(trans_add: List[Dict[str, str]]) -> None:
    """
    Запрашивает данные у пользователя и добавляет новую транзакцию.
    """
    date_input = input("Введите дату (ГГГГ-ММ-ДД): ")
    date = validate_date(date_input)
    if date is None:
        return  # Возвращаемся, если дата некорректна

    print("Выберите категорию:\n 1. Доход\n 2. Расход")
    category_choice = input("Ваш выбор (1 или 2): ")
    category = 'Доход' if category_choice == '1' else 'Расход'

    amount_input = input("Введите сумму: ")
    amount = validate_amount(amount_input)
    if amount is None:
        return  # Возвращаемся, если сумма некорректна

    description = input("Введите описание: ")
    new_transaction = {'Дата': date, 'Категория': category, 'Сумма': amount, 'Описание': description}
    trans_add = add_transaction(trans_add, new_transaction)
    save_transactions('data/transactions.csv', trans_add)
    print("Транзакция добавлена.")
    time.sleep(0.5)  # Задержка на 0.5 секунды
    input("Нажмите любую клавишу для продолжения...")


def handle_edit_transaction(trans_edit):
    """
    Обрабатывает редактирование существующей транзакции.
    """
    while True:
        index_input = input("Введите номер транзакции для редактирования (или нажмите Enter для отмены): ")
        if index_input == "":
            print("Редактирование отменено.")
            return
        try:
            transaction_index = int(index_input) - 1
            if 0 <= transaction_index < len(trans_edit):
                break
            else:
                print("Неверный номер транзакции. Пожалуйста, попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите корректный числовой индекс.")

    date_input = input("Введите новую дату (ГГГГ-ММ-ДД): ")
    date = validate_date(date_input)
    if date is None:
        return

    print("Выберите новую категорию:\n 1. Доход\n 2. Расход")
    category_choice = input("Ваш выбор (1 или 2): ")
    category = 'Доход' if category_choice == '1' else 'Расход'

    amount_input = input("Введите новую сумму: ")
    amount = validate_amount(amount_input)
    if amount is None:
        return

    description = input("Введите новое описание: ")
    updated_transaction = {'Дата': date, 'Категория': category, 'Сумма': amount, 'Описание': description}
    edit_transaction(trans_edit, transaction_index, updated_transaction)
    save_transactions('data/transactions.csv', trans_edit)
    print("Транзакция обновлена.")
    time.sleep(0.5)  # Задержка на 0.5 секунды
    input("Нажмите любую клавишу для продолжения...")


def handle_list_transactions(trans_list):
    """
    Обрабатывает вывод всех транзакций.
    """
    print("\nСписок всех транзакций:")
    transactions_info = list_transactions(trans_list)
    print(transactions_info)
    time.sleep(0.5)  # Задержка на 0.5 секунды
    input("Нажмите любую клавишу для продолжения...")


def handle_clear_transactions():
    """
    Удаляет все транзакции и сохраняет изменения в файл.
    """
    global transactions  # Используем глобальную переменную, если она введена
    transactions = clear_transactions()  # Очищаем транзакции
    save_transactions('data/transactions.csv', transactions)  # Сохраняем пустой список в файл
    print("Все транзакции были успешно удалены.")
    time.sleep(0.5)  # Задержка на 0.5 секунды
    input("Нажмите любую клавишу для продолжения...")


def handle_search_transactions():
    """
    Обрабатывает поиск транзакций по заданным критериям.
    """
    print("Введите критерии поиска:")
    print("Категория:\n 1. Доход\n 2. Расход\n 3. Любая")
    category_choice = input("Ваш выбор (оставьте пустым для всех): ")
    category = None
    if category_choice == '1':
        category = 'Доход'
    elif category_choice == '2':
        category = 'Расход'
    elif category_choice == '3' or category_choice == '':
        category = None

    date = input("Дата (оставьте пустым, если не требуется): ")
    amount = input("Сумма (оставьте пустым, если не требуется): ")
    try:
        amount = int(amount) if amount else None
    except ValueError:
        print("Некорректное значение суммы. Поиск будет выполнен без учета суммы.")
        amount = None

    filtered_transactions = search_transactions(transactions, category, date, amount)
    if filtered_transactions:
        for transaction in filtered_transactions:
            print_transaction(transaction)
    else:
        print("Транзакции не найдены.")
    time.sleep(0.5)  # Задержка на 0.5 секунды
    input("Нажмите любую клавишу для продолжения...")


def main():
    global transactions
    transactions = load_transactions('data/transactions.csv')
    while True:
        print_menu()
        choice = input("Выберите действие: ")
        if choice == '1':
            balance = calculate_balance(transactions)
            print(f"Баланс: {balance['Баланс']}, Доходы: {balance['Доходы']}, Расходы: {balance['Расходы']}")
            time.sleep(0.5)  # Задержка на 0.5 секунды
            input("Нажмите любую клавишу для продолжения...")
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
