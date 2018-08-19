class Error(Exception):
    """
    Base error class for TTT
    """
    pass

class InvalidActionError(Error):
    """
    Raised when a player attempts to make an invalid move such as:
        Coordinates are outside the board
        There is already a piece in that position
    """
    pass

class InvalidCoordinateValueError(Error):
    """
    Raised when the x and y values for a coordinate are not
    positive integers
    """
    pass

class InvalidCoordinateLengthError(Error):
    """
    Raised when there are too many or too few coordinate components
    """
    pass