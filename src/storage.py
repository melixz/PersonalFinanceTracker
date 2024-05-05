import csv
from typing import List, Dict


def load_transactions(filepath: str) -> List[Dict[str, str]]:
    """Загрузка транзакций из CSV файла."""
    transactions = []
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            transactions = [row for row in reader]
    except FileNotFoundError:
        print("Файл данных не найден. Будет создан новый файл.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
    return transactions


def save_transactions(filepath: str, transactions: List[Dict[str, str]]) -> None:
    """Сохранение списка транзакций в CSV файл."""
    try:
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['Дата', 'Категория', 'Сумма', 'Описание']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in transactions:
                writer.writerow(transaction)
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


# Пример использования:
if __name__ == "__main__":
    transactions = load_transactions('data/transactions.csv')
    print(transactions)  # Выведет список транзакций
