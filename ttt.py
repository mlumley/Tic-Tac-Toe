def makeBoard(size):
    return [['.' for i in range(size)] for j in range(size)]

def printBoard(board):
    print("Here's the current board:")
    for row in board:
        print(' '.join(row))
    print('\n')

def getUserInput(player):
    action = input("Player " + player[0] + " enter a coord x,y to place your " + player[1] + " or enter 'q' to give up: ")
    # Think about this
    if action == 'q':
        print("Exiting")
        exit()

    action = action.split(',')

    try:
        return (int(action[0]) - 1, int(action[1]) - 1)
    except:
        return None 

def validateAction(coords, board):
    if coords is None:
        print("Error: Invalid coord format. Try again")
        return False

    if coords[0] < 0 or coords[0] > len(board) and coords[1] < 0 or coords[1] > len(board):
        print("Error: Please enter a coord x,y between 1 and " + str(len(board)))
        return False
    
    if board[coords[0]][coords[1]] != '.':
        print("Error: There is already a piece at this position. Try again")
        return False

    return True


def hasWon(board):
    won = False

    # Check rows
    for row in board:
        if row[1:] == row[:-1] and row[0] != '.':
            won = True
    
    # Check columns
    tBoard = map(list, zip(*board))
    for row in tBoard:
        if row[1:] == row[:-1] and row[0] != '.':
            won = True

    # Check diagonals
    diagDown = []
    diagUp = []
    for i in range(0, len(board)):
        diagDown.append(board[i][i])
        diagUp.append(board[i][len(board)-i-1])
    if diagDown[1:] == diagDown[:-1] and diagDown[0] != '.' or diagUp[1:] == diagUp[:-1] and diagUp[0] != '.':
        won = True

    return won

def hasDrawn(board, numMoves):
    return numMoves >= len(board)**2


def main():
    board = makeBoard(3)

    player1 = ('1', 'X')
    player2 = ('2', 'O')

    player1Turn = True

    numMoves = 0

    print("Welcome to Tic Tac Toe!")
    printBoard(board)

    while(True):
        if player1Turn:
            coords = getUserInput(player1)
            if validateAction(coords, board):
                board[coords[0]][coords[1]] = player1[1]
                numMoves += 1
            else:
                printBoard(board)
                continue
        else:
            coords = getUserInput(player2)
            if validateAction(coords, board):
                board[coords[0]][coords[1]] = player2[1]
                numMoves += 1
            else:
                printBoard(board)
                continue

        if hasWon(board):
            print("Well done you've won the game!")
            printBoard(board)
            exit()

        if hasDrawn(board, numMoves):
            print("The game is drawn!")
            printBoard(board)
            exit()

        player1Turn = not player1Turn

        printBoard(board)

main()