from Board import Board 
from Player import HumanPlayer, ComputerPlayer
from numbers import Number

class Game:
    currPlayer = None
    board = Board( [None, None, None, None, None, None, None, None, None])
    player1 = None
    player2 = None
    score = {}
    mode = None
    winner = None
    gameIsOn = True
  
    
    def start(self):
        self.__chooseMode() 
        self.__setUpPlayers() 
        self.currPlayer = self.__whoGoesFirst()
        print(f" {self.currPlayer.getName()} you go first")
        if (self.mode == 1 and isinstance(self.currPlayer,ComputerPlayer)):
            randomMove = self.currPlayer.askForRandomMove(self.board)
            self.board.setCell(randomMove, self.currPlayer.getMark())
            self.__endTurn()
        while self.gameIsOn:
            self.playCurrentTurn()

    def playCurrentTurn(self):
        move = self.currPlayer.askForPlayerMove(self.board)
        print("move", move)
        if (move >=0 or move <=8):
            self.board.setCell(move, self.currPlayer.getMark())
            self.__endTurn()
        else:
            self.gameIsOn = False
            self.__endTurn()

    def __chooseMode(self):
        self.mode = int(input("please choose how many players to play? "))

    def __setUpPlayers(self):
        if self.mode == 1:
            name = input(" player1 please insert your name:")
            self.player1 = HumanPlayer(name, "X")
            self.player2 = ComputerPlayer("computer","O" )
            print("mark","O")
        elif self.mode == 2:
            name = input("player1 please insert your name:")
            self.player1 = HumanPlayer(name, "X" )
            name = input(" player2 please insert your name:")
            self.player2 = HumanPlayer(name, "O")
        
    
    def __endTurn(self):
        self.board.printboardArray()
        if (self.board.checkIfWin()):
            print(f"The winner is {self.currPlayer.getName()}")
            self.gameIsOn = False
        elif (self.board.checkIfTie()):
            print("It is a tie!")
            self.gameIsOn = False
        else:
            if (self.currPlayer == self.player1):
                self.currPlayer = self.player2
            else:
                self.currPlayer = self.player1

    def __whoGoesFirst(self):
        import random
        if random.randint(0, 1) == 0:
            return self.player1  
        else:
            return self.player2
       

game = Game()
game.start()