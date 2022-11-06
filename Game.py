from Board import Board 
from ScoreTable import ScoreTable
from Player import HumanPlayer, ComputerPlayer
from numbers import Number
import random

class Game:
    currPlayer = None
    board = Board( [None, None, None, None, None, None, None, None, None])
    player1 = None
    player2 = None
    score = ScoreTable()
    mode = None
    gameIsOn = True
    didAsk = False

    def start(self):
        self.__chooseMode() 
        self.__setUpPlayers() 
        self.currPlayer = self.__whoGoesFirst()
        print(f" {self.currPlayer.getName()} you go first")
        if (self.mode == 1 and isinstance(self.currPlayer,ComputerPlayer)):
            randomMove = self.currPlayer.askForRandomMove(self.board)
            self.board.setCell(randomMove, self.currPlayer.getMark())
            self.__endTurn()
        while self.gameIsOn or not self.didAsk:
            if self.askToContinue():
                self.playCurrentTurn()

    def askToContinue(self):
        if not self.gameIsOn:
            result = input("Do you want to play again? (y/n/s): ")
            if result != "y" and result != "s" and result != "n":
                return self.askToContinue()
            if result == "showScores" or result == "s":
                print(self.score) 
                return self.askToContinue()   
            if result == 'y':
                self.board = Board([None, None, None, None, None, None, None, None, None])
                self.gameIsOn = True
            else:
                self.didAsk = True
            return result == 'y'
        return True

    def playCurrentTurn(self):
        move = self.currPlayer.askForPlayerMove(self.board)
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
        elif self.mode == 2:
            name = input("player1 please insert your name:")
            self.player1 = HumanPlayer(name, "X" )
            name = input(" player2 please insert your name:")
            self.player2 = HumanPlayer(name, "O")
        self.score.addPlayer(self.player1)
        self.score.addPlayer(self.player2)

    
    def __endTurn(self):
        self.board.printboardArray()
        if (self.board.checkIfWin()):
            print(f"The winner is {self.currPlayer.getName()}")
            self.score.addScore(self.currPlayer, 2)
            self.gameIsOn = False
        elif (self.board.checkIfTie()):
            print("It is a tie!")
            self.score.addScore(self.player1, 1)
            self.score.addScore(self.player2, 1)
            self.gameIsOn = False
        else:
            if (self.currPlayer == self.player1):
                self.currPlayer = self.player2
            else:
                self.currPlayer = self.player1

    def __whoGoesFirst(self):
        if random.randint(0, 1) == 0:
            return self.player1  
        else:
            return self.player2
       

