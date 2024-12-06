class Stock:
    def __init__(self, ticker: str, current_price: float):
        self.__ticker = ticker
        self.__current_price = current_price # Need to either set the price manually or get the price from an API call

# Getters
    def get_ticker(self) -> str:
        return self.__ticker
    def get_price(self) -> float:
        return self.__current_price
    
# Setter
    def __set_price(self, amount) -> None:
        self.__current_price = amount

# Data Manipulation
    def __update_price(self):
        pass
        # Need to either set the price manually or get the price from an API call
        # If automated and using an API, will need a method that is constantly running to get the data