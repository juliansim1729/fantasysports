class StockNotFound(Exception):
    """Raised when the desired stock is not found within the currently recognized stocks in the system."""
    pass

class NotEnoughLiquidCash(Exception):
    """Raised when the player does not have enough liquid cash to buy the stocks or to pay the required taxes."""
    pass
