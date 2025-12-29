from accounts import Account
import gradio as gr

class TradingApp:
    def __init__(self):
        self.account = Account(owner="Trader", initial_deposit=1000.0)

    def deposit_funds(self, amount):
        try:
            self.account.deposit(amount)
            return f"Successfully deposited ${amount:.2f}. Current balance: ${self.account.balance:.2f}"
        except ValueError as e:
            return str(e)

    def withdraw_funds(self, amount):
        try:
            self.account.withdraw(amount)
            return f"Successfully withdrew ${amount:.2f}. Current balance: ${self.account.balance:.2f}"
        except ValueError as e:
            return str(e)

    def buy_shares(self, symbol, quantity):
        try:
            self.account.buy_shares(symbol, quantity)
            return f"Successfully bought {quantity} of {symbol}. Current Portfolio: {self.account.get_holdings()}"
        except ValueError as e:
            return str(e)

    def sell_shares(self, symbol, quantity):
        try:
            self.account.sell_shares(symbol, quantity)
            return f"Successfully sold {quantity} of {symbol}. Current Portfolio: {self.account.get_holdings()}"
        except ValueError as e:
            return str(e)

    def portfolio_value(self):
        return f"Total Portfolio Value: ${self.account.get_portfolio_value():.2f}"

    def profit_loss(self):
        return f"Profit/Loss: ${self.account.get_profit_loss():.2f}"

    def holdings(self):
        return self.account.get_holdings()

    def transactions(self):
        return self.account.get_transaction_history()


trading_app = TradingApp()

with gr.Blocks() as app:
    gr.Markdown("# Trading Simulation Platform")
    
    with gr.Tab("Account Management"):
        deposit_amount = gr.Number(label="Deposit Amount", value=100)
        deposit_button = gr.Button("Deposit Funds")
        deposit_output = gr.Textbox(label="Deposit Result", interactive=False)

        withdraw_amount = gr.Number(label="Withdraw Amount", value=100)
        withdraw_button = gr.Button("Withdraw Funds")
        withdraw_output = gr.Textbox(label="Withdraw Result", interactive=False)

        deposit_button.click(trading_app.deposit_funds, inputs=deposit_amount, outputs=deposit_output)
        withdraw_button.click(trading_app.withdraw_funds, inputs=withdraw_amount, outputs=withdraw_output)

    with gr.Tab("Trading Actions"):
        buy_symbol = gr.Textbox(label="Stock Symbol (AAPL, TSLA, GOOGL)")
        buy_quantity = gr.Number(label="Quantity", value=1)
        buy_button = gr.Button("Buy Shares")
        buy_output = gr.Textbox(label="Buy Result", interactive=False)

        sell_symbol = gr.Textbox(label="Stock Symbol (AAPL, TSLA, GOOGL)")
        sell_quantity = gr.Number(label="Quantity", value=1)
        sell_button = gr.Button("Sell Shares")
        sell_output = gr.Textbox(label="Sell Result", interactive=False)

        buy_button.click(trading_app.buy_shares, inputs=[buy_symbol, buy_quantity], outputs=buy_output)
        sell_button.click(trading_app.sell_shares, inputs=[sell_symbol, sell_quantity], outputs=sell_output)

    with gr.Tab("Portfolio & Transactions"):
        portfolio_value_button = gr.Button("Get Portfolio Value")
        portfolio_output = gr.Textbox(label="Portfolio Value", interactive=False)

        profit_loss_button = gr.Button("Get Profit/Loss")
        profit_loss_output = gr.Textbox(label="Profit/Loss Statement", interactive=False)

        holdings_button = gr.Button("Get Current Holdings")
        holdings_output = gr.Textbox(label="Current Holdings", interactive=False)

        transactions_button = gr.Button("Get Transaction History")
        transactions_output = gr.Textbox(label="Transaction History", interactive=False)

        portfolio_value_button.click(trading_app.portfolio_value, outputs=portfolio_output)
        profit_loss_button.click(trading_app.profit_loss, outputs=profit_loss_output)
        holdings_button.click(trading_app.holdings, outputs=holdings_output)
        transactions_button.click(trading_app.transactions, outputs=transactions_output)

app.launch()