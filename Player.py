from Board import Board 
from numbers import Number

class Player:
    array = []

    def __init__(self, name, mark):
        self.__name = name
        self.__mark = mark 
 
    def getMark(self):
        return self.__mark
    
    def getName(self):
        return self.__name
    
    def askForPlayerMove(self,board):
        pass

    def askForRandomMove(self,board):
        import random
        move = random.randrange(0,9)
        if board.getCell(move) != None:
            return self.askForRandomMove(board)
        else:
            return move


class HumanPlayer(Player):

    def askForPlayerMove(self,board):
        canPlay = False
        for i in board.getBoard():
            if i == None:
                canPlay = True
                break
        if not canPlay:
            return False
        move = int(input(f"player please enter number between 0-8: "))
        print(move)
        if move > 8 or move < 0 or board.getCell(move)!= None:  
            return self.askForPlayerMove(board)
        if move >=0 and move <=8:
            if board.getCell(move) == None:
                return move

  
class ComputerPlayer(Player):

    def askForPlayerMove(self,board):
        mark = self.getMark()
        if mark == "O":
             mark = "X"
        else:
            mark = "O"
        move = self.canWinNextMove(board,mark)
        if move != False:
            return move
        move = self.checkForBlockThePlayer(board)
        if move != False:
            return move
        move = self.checkForCorners(board)
        if move != False:
            return move
        if board.getCell(4) == None:
            move = 4
            return move
        move = self.checkForSides(board)
        if move != False:
            return move
        return False
                    
    def canWinNextMove(self,board,mark):
        for i in range(0, 9):
                boardCopy = self.getDuplicate(board)
                print("checkboard",boardCopy.boardArray)
                if boardCopy.boardArray[i] == None:
                    boardCopy.setCell(i,mark)
                    if boardCopy.checkIfWin(): 
                        print(i, "check" )
                        return i       
        return False

    def getDuplicate(self ,board):
        return Board(board.getBoard())
      
    def checkForBlockThePlayer(self,board):
        mark = self.getMark()
        if mark == "O":
            mark = "X"
        else: 
            mark = "O"
        return self.canWinNextMove(board,mark)

            
    def isSpaceFree(self,board,move):
        return board[move] == None
    
   
    def checkForCorners(self,board):
        for i in [0,2,6,8]:
            if board.boardArray[i] == None:
                print("check",board.boardArray[i])
                return i
        return False

    def checkForSides(self,board):
        for i in [1,3,5,7]:
            if board.boardArray[i] == None:
                return i
        return False
       
    def setCopyCell(self,copy,cellNumber,mark):
        copy[cellNumber] = mark

    def RemoveCopyCell(self,copy,cellNumber):
        copy[cellNumber] = None

   


    








    



# b1 = Board()
# b1.printBoard()
# p1 = HumanPlayer("Hila" , "X" , b1) 
# p2 = ComputerPlayer("comp" , "O" , b1) 

# p1.action(6)
# p2.action()
# b1.printBoard()
