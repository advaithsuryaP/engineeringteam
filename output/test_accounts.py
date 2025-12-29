import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('John Doe', 1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)
        with self.assertRaises(ValueError):
            self.account.deposit(-100.0)

    def test_withdraw(self):
        self.account.withdraw(200.0)
        self.assertEqual(self.account.balance, 800.0)
        with self.assertRaises(ValueError):
            self.account.withdraw(1000.0)
        with self.assertRaises(ValueError):
            self.account.withdraw(-50.0)

    def test_buy_shares(self):
        self.account.buy_shares('AAPL', 2)  # 2 shares at 150 each
        self.assertEqual(self.account.balance, 700.0)
        self.assertEqual(self.account.get_holdings(), {'AAPL': 2})
        with self.assertRaises(ValueError):
            self.account.buy_shares('AAPL', 10)  # Not enough funds

    def test_sell_shares(self):
        self.account.buy_shares('TSLA', 1)  # Buy 1 share at 700
        self.account.sell_shares('TSLA', 1)  # Sell 1 share
        self.assertEqual(self.account.balance, 1000.0)
        with self.assertRaises(ValueError):
            self.account.sell_shares('TSLA', 1)  # Not enough shares

    def test_get_portfolio_value(self):
        self.account.buy_shares('GOOGL', 1)  # 2800
        self.assertEqual(self.account.get_portfolio_value(), 3800.0)

    def test_get_profit_loss(self):
        self.account.buy_shares('AAPL', 1)  # Buy 1 share
        self.account.deposit(500.0)  # More funds
        self.assertGreater(self.account.get_profit_loss(), -1000.0)

    def test_get_transaction_history(self):
        self.account.deposit(500.0)
        self.account.withdraw(200.0)
        self.assertEqual(len(self.account.get_transaction_history()), 2)

if __name__ == '__main__':
    unittest.main()