# Error for when user tries to do something when they do not have the funds to do so
class InsufficientFundsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ImproperCredentialsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

