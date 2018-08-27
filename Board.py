from Error import InvalidActionError


class Board():
    """
    Represents a square board of size n that players can mark their symbol on
    to play Tic-Tac-Toe
    """

    def __init__(self, size, emptyBoardSpace):
        self.board = [
            [emptyBoardSpace for i in range(size)] for j in range(size)]
        self.numMoves = 0
        self.emptyBoardSpace = emptyBoardSpace

    def printBoard(self):
        print("\nHere's the current board:")

        print("  ", end="")
        for i in range(1, len(self.board) + 1):
            print(i, end=" ")
        print("")

        i = 1
        for row in self.board:
            print(str(i) + " " + ' '.join(row))
            i += 1

    def markBoard(self, player, coordinate):
        """
        Places the player's symbol at the coordinate on the board
        """
        self.validateAction(coordinate)
        self.board[coordinate.x][coordinate.y] = player.symbol
        self.numMoves = self.numMoves + 1

    def validateAction(self, coordinate):
        """
        Validate that the coordinate is a valid position on the board
        and unoccupied
        """
        xNotInBoardRange = coordinate.x < 0 or coordinate.x >= len(self.board)
        yNotInBoardRange = coordinate.y < 0 or coordinate.y >= len(self.board)

        if xNotInBoardRange or yNotInBoardRange:
            raise InvalidActionError(
                (
                    "Error: Please enter a coordinate x,y with values"
                    " between 1 and " + str(len(self.board))
                )
            )

        elif self.board[coordinate.x][coordinate.y] != self.emptyBoardSpace:
            raise InvalidActionError(
                "Error: There is already a piece at this position. Try again"
            )

    def hasWon(self):
        return self.checkRows() or self.checkColumns() or self.checkDiagonals()

    def checkAllElementsSame(self, lst):
        """
        Check that all elements of a list are the same and not empty spaces
        """
        numUniqueElements = len(set(lst))
        notEmptySpace = lst[0] != self.emptyBoardSpace
        if numUniqueElements == 1 and notEmptySpace:
            return True

    def checkRows(self):
        for row in self.board:
            if self.checkAllElementsSame(row):
                return True

    def checkColumns(self):
        tBoard = map(list, zip(*self.board))
        for col in tBoard:
            if self.checkAllElementsSame(col):
                return True

    def checkDiagonals(self):
        diagLeftRight = []
        diagRightLeft = []
        for i in range(0, len(self.board)):
            diagLeftRight.append(self.board[i][i])
            diagRightLeft.append(self.board[i][len(self.board)-i-1])
        if self.checkAllElementsSame(diagLeftRight) \
           or self.checkAllElementsSame(diagRightLeft):
            return True

    def hasDrawn(self):
        return self.numMoves >= len(self.board)**2
