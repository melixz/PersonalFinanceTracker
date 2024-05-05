from typing import List, Dict, Optional


def add_transaction(transactions: List[Dict[str, str]], new_transaction: Dict[str, str]) -> List[Dict[str, str]]:
    """
    Добавляет новую транзакцию в список транзакций.

    :param transactions: Список текущих транзакций.
    :param new_transaction: Словарь с данными новой транзакции.
    :return: Обновлённый список транзакций.
    """
    transactions.append(new_transaction)
    return transactions


def edit_transaction(transactions: List[Dict[str, str]], transaction_index: int, updated_transaction: Dict[str, str]) -> \
        List[Dict[str, str]]:
    """
    Редактирует существующую транзакцию в списке по указанному индексу.

    :param transactions: Список текущих транзакций.
    :param transaction_index: Индекс редактируемой транзакции.
    :param updated_transaction: Словарь с обновлёнными данными транзакции.
    :return: Обновлённый список транзакций.
    """
    if 0 <= transaction_index < len(transactions):
        transactions[transaction_index] = updated_transaction
    return transactions


def search_transactions(transactions: List[Dict[str, str]], category: Optional[str] = None, date: Optional[str] = None,
                        amount: Optional[int] = None) -> List[Dict[str, str]]:
    """
    Ищет транзакции по заданным критериям.

    :param transactions: Список транзакций.
    :param category: Категория для поиска.
    :param date: Дата для поиска.
    :param amount: Сумма для поиска.
    :return: Список транзакций, соответствующих критериям.
    """
    filtered_transactions = []
    for transaction in transactions:
        if (category is None or transaction['Категория'] == category) and \
                (date is None or transaction['Дата'] == date) and \
                (amount is None or int(transaction['Сумма']) == amount):
            filtered_transactions.append(transaction)
    return filtered_transactions


def calculate_balance(transactions: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Рассчитывает общий баланс, сумму доходов и расходов.

    :param transactions: Список транзакций.
    :return: Словарь с ключами 'Баланс', 'Доходы', 'Расходы'.
    """
    balance = {'Баланс': 0, 'Доходы': 0, 'Расходы': 0}
    for transaction in transactions:
        cleaned_sum = transaction['Сумма'].replace(' ', '')  # Удаление пробелов
        if transaction['Категория'] == 'Доход':
            balance['Доходы'] += int(cleaned_sum)
        elif transaction['Категория'] == 'Расход':
            balance['Расходы'] += int(cleaned_sum)
    balance['Баланс'] = balance['Доходы'] - balance['Расходы']
    return balance


def list_transactions(transactions):
    """
    Возвращает строку, содержащую список всех транзакций с номерами.

    :param transactions: список словарей, каждый из которых представляет транзакцию.
    :return: строка с пронумерованным списком транзакций.
    """
    result = []
    for index, transaction in enumerate(transactions, start=1):
        transaction_info = (
            f"{index}. Дата: {transaction['Дата']}\n"
            f"    Категория: {transaction['Категория']}\n"
            f"    Сумма: {transaction['Сумма']}\n"
            f"    Описание: {transaction['Описание']}\n"
        )
        result.append(transaction_info)
    return "\n".join(result)


def clear_transactions():
    """
    Очищает все сохраненные транзакции.

    :return: Пустой список транзакций.
    """
    return []
