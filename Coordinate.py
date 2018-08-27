from Error import InvalidCoordinateValueError


class Coordinate():
    """
    Represents a x, y coordinate
    """

    def __init__(self, x, y):
        self.x = self.validate(x)
        self.y = self.validate(y)

    def validate(self, val):
        """
        Validate that val is an integer
        """
        try:
            return int(val)
        except:
            raise InvalidCoordinateValueError(
                (
                    "Error: Invalid coordinate values. "
                    "Coordinates should be integer values"
                )
            )

    def subtract(self, val):
        """
        Subtract val from x and y
        """
        self.x = self.x - val
        self.y = self.y - val
