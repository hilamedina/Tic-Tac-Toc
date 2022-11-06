from Board import Board 
# from Enums import Mark
class Player:
    def __init__(self, name, mark, board):
        self.__name = name
        self.__mark = mark 
        self.__board = board

    def getMark(self):
        return self.__mark

    def getName(self):
        return self.__name

    def makeRandomMove(self):
        pass

    def makePlayerTurn(self, board):
        pass
        
class HumanPlayer(Player):
    def makeRandomMove(self, board):
        return False
    
    def makePlayerTurn(self, board):
        # self.move = int(input(f"player:" + {self.currPlayer.name} +  "please enter number between 0-8 "))
       move = int(input(f"player please enter number between 0-8 "))
       if move >=0 and move <=8 and board.getCell(move) == None:
            board.setCell(move, self.getMark()) 
            print(board)

class ComputerPlayer(Player):
    def makeRandomMove(self, board):
        import random
        cellNumber = random.randint(0,8)
        board.setCell(cellNumber, self.getMark())
        return True

    def makePlayerTurn(self, board):
        pass
    

        # if self.__board[0] == "X" and self.__board[1] == "X":
        #     self.currPlayer = self.__board[2] = "O" # ROW1
            
        # elif self.__board[3] == "X" and self.__board[4] == "X":
        #     self.currPlayer = self.__board[5] = "0" # ROW2
            
        # elif self.__board[6] == "X" and self.__board[7] == "X":
        #     self.currPlayer = self.__board[8] = "X" # ROW3
            
        # elif self.__board[0] == "X" and self.__board[3] == "O":
        #     self.currPlayer = self.__board[6] = "X" # COL1
            
        # elif self.__board[1] == "x" and self.__board[4] == "X":
        #     self.currPlayer = self.__board[7] = "0" # COL2
            
        # elif self.__board[2] == "X" and self.__board[5] == "X":
        #     self.currPlayer = self.__board[8] = "X" #COL3
            
        # elif self.__board[0] == "X" and self.__board[4] == "X":
        #     self.currPlayer = self.__board[8] = "O" #DIAGONAL1
            
        # elif board [2] == "O" and board[4] =="O":
        #     self.currPlayer = self.__board[6] = "X" #diagonal2
        
      












# b1 = Board()
# b1.printBoard()
# p1 = HumanPlayer("Hila" , "X" , b1) 
# p2 = ComputerPlayer("comp" , "O" , b1) 

# p1.action(6)
# p2.action()
# b1.printBoard()


  