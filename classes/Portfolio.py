from Stock import Stock

class Portfolio:
    def __init__(self):
        self.__net_value = 0
        self.__owned_stock = None

    # Setters
    def __set_net_value(self, number):
        self.__net_value += number

    # Getters
    def display_net(self) -> int:
        return self.__net_value
    
    def add_stock(self, Stock, shares):
        pass
    def remove_stock(self, Stock, shares):
        pass