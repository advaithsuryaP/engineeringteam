# accounts.py

class Account:
    def __init__(self, owner: str, initial_deposit: float):
        """
        Initialize a new account with owner's name and an initial deposit.
        
        :param owner: Name of the account owner
        :param initial_deposit: Initial amount of money deposited into the account
        """
        self.owner = owner
        self.balance = initial_deposit
        self.portfolio = {}  # dictionary to hold holdings {symbol: quantity}
        self.transactions = []  # list to hold transaction history
        
    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.
        
        :param amount: Amount to be deposited
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        
    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the account.
        
        :param amount: Amount to be withdrawn
        """
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")

    def buy_shares(self, symbol: str, quantity: int) -> None:
        """
        Buy shares of a specified stock.
        
        :param symbol: The stock symbol to buy shares of
        :param quantity: The number of shares to buy
        """
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity
        if self.balance < total_cost:
            raise ValueError("Insufficient funds to buy shares.")
        
        self.balance -= total_cost
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
        self.transactions.append(f"Bought {quantity} of {symbol} at {share_price} each")

    def sell_shares(self, symbol: str, quantity: int) -> None:
        """
        Sell shares of a specified stock.
        
        :param symbol: The stock symbol to sell shares of
        :param quantity: The number of shares to sell
        """
        if symbol not in self.portfolio or self.portfolio[symbol] < quantity:
            raise ValueError("You do not own enough shares to sell.")
        
        share_price = get_share_price(symbol)
        self.portfolio[symbol] -= quantity
        if self.portfolio[symbol] == 0:
            del self.portfolio[symbol]
        
        self.balance += share_price * quantity
        self.transactions.append(f"Sold {quantity} of {symbol} at {share_price} each")

    def get_portfolio_value(self) -> float:
        """
        Calculate the total value of the user's portfolio.
        
        :return: Total value of the portfolio
        """
        total_value = self.balance
        for symbol, quantity in self.portfolio.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def get_profit_loss(self) -> float:
        """
        Calculate the profit or loss from the initial deposit.
        
        :return: Profit or loss amount
        """
        initial_investment = self.balance + sum(get_share_price(symbol) * quantity for symbol, quantity in self.portfolio.items())
        return self.get_portfolio_value() - initial_investment

    def get_holdings(self) -> dict:
        """
        Report the current holdings of the user.
        
        :return: A dictionary of stock holdings {symbol: quantity}
        """
        return self.portfolio

    def get_profit_loss_statement(self) -> float:
        """
        Get the profit or loss statement.
        
        :return: Profit or loss from initial deposit
        """
        return self.get_profit_loss()

    def get_transaction_history(self) -> list:
        """
        List all transactions made by the user.
        
        :return: A list of transactions
        """
        return self.transactions

def get_share_price(symbol: str) -> float:
    """
    Return the current share price for a given stock symbol.
    
    :param symbol: The stock symbol to get the price for
    :return: The price of the stock
    """
    share_prices = {
        "AAPL": 150.0,
        "TSLA": 700.0,
        "GOOGL": 2800.0
    }
    return share_prices.get(symbol, 0.0)  # Returns 0.0 if symbol is not found