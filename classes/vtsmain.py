from vtsTransaction import Transaction
from vtsPortfolio import Portfolio
from vtsStock import Stock
from vtsUser import User
from vtsErrors import ImproperCredentialsError

class main:
    print("Welcome to the Virtual Stock Trading Simulator. Please enter your account credentials.")

    username = input("Enter Username: ")
    if username is "":
        raise ImproperCredentialsError(f"Improper user. Ensure Username and Password are valid")
    

    password = input("Enter Password: ")
    if password is "":
        raise ImproperCredentialsError(f"Improper password. Ensure Username and Password are valid")

    def __init__(self, username, password):
        user = User(username, password)

    
    
    


