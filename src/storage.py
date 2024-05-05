import csv
import os
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


def save_transactions(filepath: str, transactions):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Убедитесь, что директория существует
    fieldnames = ['Дата', 'Категория', 'Сумма', 'Описание']
    try:
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in transactions:
                writer.writerow(transaction)
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


# Пример использования:
if __name__ == "__main__":
    transactions = load_transactions('data/transactions.csv')
    print(transactions)  # Выведет список транзакций
