class Error(Exception):
    """Base class for other customized errors."""
    pass

class StockNotFoundError(Error):
    """Raised when the desired stock is not found within the currently recognized stocks in the system."""
    pass

class NotEnoughLiquidCashError(Error):
    """Raised when the player does not have enough liquid cash to buy the stocks or to pay the required taxes."""
    pass

class NotEnoughAssetsError(Error):
    """Raised when the player does not have enough assets to sell."""
    pass

class InvalidValueSubmissionError(Error):
    """Raised when an invalid value is submitted."""
    pass
