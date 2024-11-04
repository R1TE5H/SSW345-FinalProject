from typing import List
from Errors import InsufficientFundsError
from Transaction import Transaction

class User:
    def __init__(self, username, password, purchasingPower=0.00,transactions=None, portfolio=None):
        self.__username = username
        self.__password = password
        self.__transactions = transactions
        self.__portfolio = portfolio
        self.__purchasing_power = purchasingPower

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
    
    def get_transactions(self) -> List[Transaction]:
        return self.__transactions 

    def get_portfolio(self) -> Portfolio:
        return self.__portfolio

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
