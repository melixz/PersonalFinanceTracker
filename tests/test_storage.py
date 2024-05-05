import unittest
import os
from storage import load_transactions, save_transactions


class TestStorage(unittest.TestCase):
    def setUp(self):
        # Путь к временному тестовому файлу
        self.test_file_path = 'test_data.csv'
        # Начальные тестовые данные
        self.test_data = [
            {'Дата': '2024-01-01', 'Категория': 'Доход', 'Сумма': '5000', 'Описание': 'Зарплата'},
            {'Дата': '2024-01-02', 'Категория': 'Расход', 'Сумма': '200', 'Описание': 'Кофе'}
        ]
        # Создание тестового файла
        save_transactions(self.test_file_path, self.test_data)

    def tearDown(self):
        # Удаление тестового файла после выполнения каждого теста
        try:
            os.remove(self.test_file_path)
        except OSError:
            pass

    def test_load_transactions(self):
        # Загрузка данных из файла и проверка, что они корректны
        transactions = load_transactions(self.test_file_path)
        self.assertEqual(transactions, self.test_data)

    def test_save_transactions(self):
        # Добавление новой транзакции и сохранение в файл
        new_transaction = {'Дата': '2024-01-03', 'Категория': 'Расход', 'Сумма': '1200', 'Описание': 'Обед'}
        self.test_data.append(new_transaction)
        save_transactions(self.test_file_path, self.test_data)
        # Перезагрузка файла и проверка, что данные сохранены правильно
        saved_data = load_transactions(self.test_file_path)
        self.assertIn(new_transaction, saved_data)


if __name__ == '__main__':
    unittest.main()
