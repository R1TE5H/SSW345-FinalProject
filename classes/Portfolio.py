from Stock import Stock
from Errors import InsufficientFundsError

class Portfolio:
    def __init__(self):
        self.__net_value = 0
        self.__owned_stock = {}

    # Setters
    def __set_net_value(self, number: int):
        self.__net_value += number

    # Getters
    def get_net(self) -> int:
        return self.__net_value
    
    def get_portfolio(self):
        return {"Net Balance": self.get_net(),
                "Owned Stocks": self.get_owned_stock()}
    
    def get_owned_stock(self) -> dict:
        return self.__owned_stock
    
    def add_stock(self, stock: Stock, shares: float) -> None:
        ticker = stock.get_ticker()
        owned_stock = self.get_owned_stock()

        if stock.get_ticker() in owned_stock:
            self.__owned_stock[ticker] += shares
        else:
            self.__owned_stock[ticker] = shares

        self.__set_net_value(stock.get_price() * shares)

    def remove_stock(self, stock: Stock, shares: float) -> None:
        ticker = stock.get_ticker()
        owned_stock = self.get_owned_stock()

        if ticker in owned_stock:
            if owned_stock[ticker] > shares:
                self.__owned_stock[ticker] -= shares
                self.__set_net_value(-(stock.get_price() * shares))
            elif owned_stock[ticker] == shares:
                del self.__owned_stock[ticker] 
            else:
                raise InsufficientFundsError(f"Insufficient number of shares.")

        else:
            raise InsufficientFundsError(f"Insufficient number of shares.")