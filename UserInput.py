from Coordinate import Coordinate
from Error import InvalidCoordinateLengthError


class UserInput():
    """
    Responsible for getting and parsing user input
    """

    def processUserInput(self, player):
        """
        Get player input from the terminal and return a coordinate
        corresponding to the move or exit the game if the player
        chose to quit.
        """
        action = input(
            (
                "Player " + player.id + " enter a coord x,y"
                " to place your " + player.symbol + " or"
                " enter 'q' to give up: "
            )
        )

        if action == 'q':
            self.exitGame()

        action = action.split(',')
        numCoordinate = len(action)

        if numCoordinate != 2:
            raise InvalidCoordinateLengthError(
                (
                    "Error: Invalid coordinate length. "
                    "Coordinates should be of the format x,y"
                )
            )
        else:
            return self.listToCoordinate(action)

    def exitGame(self):
        print("Exiting")
        exit()

    def listToCoordinate(self, lst):
        coord = Coordinate(lst[0], lst[1])
        # Convert coordinate from 1 based to 0 based
        coord.subtract(1)
        return coord
