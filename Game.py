from Board import Board 
from Player import HumanPlayer, ComputerPlayer
# from Enums import GameMode , Mark

class Game:
    currPlayer = None
    board = Board()
    player1 = None
    player2 = None
    mark1 = None
    mark2 = None
    score = {}
    mode = None
    winner = None
    currentGame = True

    def start(self):
        self.__chooseMode()
        self.__setUpPlayers()
        self.__whoGoesFirst()
        if (self.mode == 1):
            if (self.currPlayer.makeRandonMoveIfComputerStart(self.board)):
                self.__endTurn()

        while self.currentGame:
            self.currPlayer.makePlayerTurn(self.board)
            self.__endTurn()
            

    def __chooseMode(self):
        self.mode = int(input("please choose how many players to play? "))

    def __setUpPlayers(self):
        self.mark1 = "X" 
        self.mark2 = "O"

        if self.mode == 1:
            name = input(" player1 please insert your name:")
            self.player1 = HumanPlayer(name, self.mark1, self.board)
            print("mark",self.mark1)
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
        if (self.board.checkIfWin()):
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
game.start()









    

