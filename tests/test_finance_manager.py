import unittest
from finance_manager import add_transaction, edit_transaction, search_transactions, calculate_balance


class TestFinanceManager(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            {'Дата': '2024-05-02', 'Категория': 'Расход', 'Сумма': '1500', 'Описание': 'Покупка продуктов'},
            {'Дата': '2024-05-03', 'Категория': 'Доход', 'Сумма': '30000', 'Описание': 'Зарплата'}
        ]

    def test_add_transaction(self):
        new_transaction = {'Дата': '2024-05-04', 'Категория': 'Доход', 'Сумма': '2000', 'Описание': 'Фриланс'}
        add_transaction(self.transactions, new_transaction)
        self.assertIn(new_transaction, self.transactions)

    def test_edit_transaction(self):
        updated_transaction = {'Дата': '2024-05-02', 'Категория': 'Расход', 'Сумма': '1600', 'Описание': 'Покупка продуктов + хлеб'}
        edit_transaction(self.transactions, 0, updated_transaction)
        self.assertEqual(self.transactions[0], updated_transaction)

    def test_search_transactions(self):
        result = search_transactions(self.transactions, category='Доход')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['Сумма'], '30000')

    def test_calculate_balance(self):
        balance = calculate_balance(self.transactions)
        self.assertEqual(balance['Баланс'], 28500)  # 30000 доход - 1500 расход


if __name__ == '__main__':
    unittest.main()
