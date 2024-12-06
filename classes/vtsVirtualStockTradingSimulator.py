from vtsTransaction import Transaction
from vtsPortfolio import Portfolio
from vtsStock import Stock
from vtsUser import User
from vtsErrors import ImproperCredentialsError

class VirtualStockTradingSimulator:
    def __init__(self):
        print("Welcome to the Virtual Stock Trading Simulator. Please enter your account credentials.")

        username = input("Enter Username: ").strip()
        if not username:
            raise ImproperCredentialsError(f"Username cannot be empty. Please provide valid credentials.")

        password = input("Enter Password: ").strip()
        if not username:
            raise ImproperCredentialsError(f"Password cannot be empty. Please provide valid credentials.")
        
        self.user = User(username, password)
        print(f"Welcome, {username}!")

        self.set_purchasing_power()

        print(f"Your current purchasing power is ${self.user.purchasing_power:.2f}")
    
        self.stock1 = Stock(ticker="AAPL",current_price=150)
        self.stock2 = Stock(ticker="GOOG", current_price=2800)

        #Add test transactions
        self.user.buy_stock(self.stock1, 10) #Buy 10 shares of AAPL
        self.user.sell_stock(self.stock1, 5) #Sell 5 shares of AAPL
        self.user.buy_stock(self.stock2, 2) #Buy 2 shares of GOOG

        self.user.print_transactions() #Displays previous transactions

    def set_purchasing_power(self):
        while True:
            try:
                amt = float(input("Set purchasing power: ").strip())
                if amt <= 0:
                    print("Purchasing power must be a positive value. Please try again.")
                else:
                    self.user.purchasing_power = amt  # Directly setting the attribute
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")



if __name__ == "__main__":
    try:
        simulator = VirtualStockTradingSimulator()
    except ImproperCredentialsError as e:
        print(f"Error: {e}")
        


    
    
    


