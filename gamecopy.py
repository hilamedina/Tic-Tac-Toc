from Board import Board
from Player import HumanPlayer, ComputerPlayer

# from Enums import GameMode , Mark

changePlayerMark = {
    "O": "X",
    "X": "O"
}


class Game:
    currPlayer = None
    board = Board()
    boards = {}
    player1 = None
    player2 = None
    mark1 = None
    mark2 = None
    score = {}
    mode = None
    winner = None
    currentGame = True

    def printBoards(self):
        print(self.board)
        for key in self.boards:
            print(key)

    def getBoard(self):
        return self.board

    def setBoards(self, board, playerMark):
        self.boards[str(board)] = board

        for index, cell in enumerate(board.getBoard()):
            if cell == None:
                newBoardArray = board.getBoard()
                newBoardArray[index] = playerMark
                newBoard = Board(newBoardArray)
                board.setNeighbor(newBoard)
                newBoard.setNeighbor(board)
                self.setBoards(newBoard, changePlayerMark[playerMark])

    def start(self):
        self.__chooseMode()
        self.__setUpPlayers()
        self.__whoGoesFirst()
        if self.mode == 1:
            if self.currPlayer.makeRandomMove(self.board):
                self.__endTurn()

        while self.currentGame:
            self.currPlayer.makePlayerTurn(self.board)
            self.__endTurn()

        self.mode = int(input("please choose how many players to play? "))

    def __setUpPlayers(self):
        self.mark1 = "X"
        self.mark2 = "O"

        if self.mode == 1:
            name = input(" player1 please insert your name:")
            self.player1 = HumanPlayer(name, self.mark1, self.board)
            print("mark", self.mark1)
            self.player2 = ComputerPlayer(name, self.mark2, self.board)
        elif self.mode == 2:
            name = input("player1 please insert your name:")
            self.player1 = HumanPlayer(name, self.mark1, self.board)
            name = input(" player2 please insert your name:")
            self.player2 = HumanPlayer(name, self.mark2, self.board)
            # print(self.player2.name)

    def __endTurn(self):
        self.board.printBoard()

        # check if game ended
        if self.board.checkIfWin():
            print(f"Winner is {self.currPlayer.getName()}")
            self.currentGame = False
        elif (self.board.checkIfTie()):
            print("It is a tie!")
            self.currentGame = False
        else:
            # switch current player
            if (self.currPlayer == self.player1):
                self.currPlayer = self.player2
            else:
                self.currPlayer = self.player1

    def __whoGoesFirst(self):
        import random
        if random.randint(0, 1) == 0:
            self.currPlayer = self.player1
            print(f"{self.player1.getName()} you go first")
        else:
            self.currPlayer = self.player2
            print(f"{self.player2.getName()} you go first")


game = Game()
# boardArray = self.board(getBoard)
newBoard = Board()
game.setBoards(newBoard, "O")
game.printBoards()
game.start()
