#!/usr/bin/env python3

from Player import Player
from Board import Board
from UserInput import UserInput
from Error import Error

BOARD_SIZE = 3

def main():
    """
    Contains the main game loop
    """
    board = Board(BOARD_SIZE)

    player1 = Player('1', 'X')
    player2 = Player('2', 'O')
    currentPlayer = player1

    userInput = UserInput()

    print("Welcome to Tic Tac Toe!")
    board.printBoard()

    while(True):
        try:
            coord = userInput.processUserInput(currentPlayer)
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