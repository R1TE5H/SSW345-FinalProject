from typing import List
from vtsErrors import InsufficientFundsError
from vtsTransaction import Transaction
from vtsPortfolio import Portfolio
from vtsStock import Stock

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__transactions: List[Transaction] = []
        self.__portfolio = Portfolio()
        self.__purchasing_power = 0.00

    def login(self, username, password):
        if (username == self.get_username() and password == self.__get_password()):
            pass
    
# Getters
    def get_username(self) -> str:
        return self.__username
    
    def __get_password(self) -> str:
        return self.__password
    
    def get_purchasing_power(self) -> float:
        return self.__purchasing_power
    
# Setters
    def __set_purchasing_power(self, amount) -> None:
        self.purchasing_power = amount

# Data Manipulation
    def deposit_funds(self, amount) -> None:
        self.purchasing_power += amount

    def withdraw_funds(self, amount) -> None:
        current_balance = self.get_purchasing_power()
        if (amount > current_balance):
            raise InsufficientFundsError(f"You do not have {amount} in your account to withdraw. Consider withdrawing less or selling stocks to meet your withdrawal needs.")
        else:
            self.__set_purchasing_power(current_balance - amount)
# Transaction Manipulation
    def add_transaction(self, stock:Stock, type: str, shares:float) -> None:
        self.__transactions.append(Transaction(shares, type, stock))
    
    def get_transactions(self) -> List[Transaction]:
        return self.__transactions 
    #  Need to figure out a way to properly print the transactions list

# Portfolio Manipulation 
    def get_portfolio(self) -> Portfolio:
        return self.__portfolio.get_portfolio()

    def buy_stock(self, stock: Stock, shares: float) -> None:
        self.__portfolio.add_stock(stock, shares)
        self.add_transaction(stock, "Buy", shares)

    def sell_stock(self, stock: Stock, shares: float) -> None:
        self.__portfolio.remove_stock(stock, shares)
        self.add_transaction(stock, "Sell", shares)


# test = User("Testing", "test")
# print(test.get_username())
# test.buy_stock(Stock("Testing", 459.00), 7.5)
# print(test.get_portfolio())
# print(test.get_transactions())
