from Coordinate import Coordinate
from Player import Player
from Board import Board
from Error import Error
from Error import InvalidCoordinateLengthError

BOARD_SIZE = 3

def processUserInput(player):
    """
    Get player input from the terminal and return a coordinate
    corispnding to the move or exit the game if the player
    chose to quit.
    """
    action = input("Player " + player.id + " enter a coord x,y to place your " + player.symbol + " or enter 'q' to give up: ")

    if action == 'q':
        print("Exiting")
        exit()

    action = action.split(',')

    if len(action) != 2:
        raise InvalidCoordinateLengthError("Error: Invalid coordinate length. Coordinates should be of the format x,y")
    else:
        coord = Coordinate(action[0], action[1])
        # Convert coordinate from 1 based to 0 based
        coord.subtract(1)
        return coord


def main():
    """
    Contains the main game loop
    """
    board = Board(BOARD_SIZE)

    player1 = Player('1', 'X')
    player2 = Player('2', 'O')
    currentPlayer = player1

    print("Welcome to Tic Tac Toe!")
    board.printBoard()

    while(True):
        try:
            coord = processUserInput(currentPlayer)
            board.markBoard(currentPlayer, coord)
            board.printBoard()
        except Error as error:
            print(error)
            board.printBoard()
            continue

        if board.hasWon():
            print("Well done Player " + currentPlayer.id + ", you've won the game!")
            board.printBoard()
            exit()

        if board.hasDrawn():
            print("There was a draw")
            board.printBoard()
            exit()

        if currentPlayer == player1:
            currentPlayer = player2
        else:
            currentPlayer = player1

main()