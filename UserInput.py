from Coordinate import Coordinate
from Error import InvalidCoordinateLengthError


class UserInput():
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
            print("Exiting")
            exit()

        action = action.split(',')

        if len(action) != 2:
            raise InvalidCoordinateLengthError(
                (
                    "Error: Invalid coordinate length."
                    " Coordinates should be of the format x,y"
                )
            )
        else:
            coord = Coordinate(action[0], action[1])
            # Convert coordinate from 1 based to 0 based
            coord.subtract(1)
            return coord
