from Board import Board 

class Player:
    board = Board()
    move = ""
    array = []
    currenGame = True
    Hila = True

    def __init__(self, name, mark, board):
        self.__name = name
        self.__mark = mark 
        self.board = board

    def getMark(self):
        return self.__mark
    
    def getName(self):
        return self.__name

    def makeRandonMoveIfComputerStart(self):
        pass

    def makePlayerTurn(self, board):
        pass

    def getDuplicate(self, board):
        pass

    def isSpaceFree(self, board ,move):
        pass

    def setCell(self, cellNumber, mark):
        Board.board[cellNumber] = mark

    def checkIfWin(self,copy):
           return self.checkRow() or self.checkDiagonal() or self.checkCol()

    def checkCol(self):
        if Board.board[0] == Board.board[1] == Board.board[2] and Board.board[0] != None:
            return True
        elif Board.board[3] == Board.board[4] == Board.board[5] and Board.board[3] != None:
            return True
        elif Board.board[6] == Board.board[7] == Board.board[8] and Board.board[6] != None:
            return True

    def checkDiagonal(self):
        if Board.board[0] == Board.board[4] == Board.board[8] and Board.board[0] != None:
            return True
        elif Board.board[2] == Board.board[4] == Board.board[6] and Board.board[4] != None:
            return True

    def checkIfTie(self):
        return None not in Board.board

    def checkRow(self):
        if Board.board[0] == Board.board[3] == Board.board[6] and Board.board[0] != None:
            return True
        elif Board.board[1] == Board.board[4] == Board.board[7] and Board.board[1] != None:
            return True
        elif Board.board[2] == Board.board[5] == Board.board[8] and Board.board[2] != None:
            return True 

    def checkForWinForComp(self):
        pass  

class HumanPlayer(Player):
    def makeRandonMoveIfComputerStart(self,board):
        return False
    
    def makePlayerTurn(self, board):
        # self.move = int(input(f"player:" + {self.currPlayer.name} +  "please enter number between 0-8 "))
       move = int(input(f"player please enter number between 0-8 "))
       print(move)
       if (move > 8 and move <0 ):  
            move = int(input("plese choose difference number:"))
            board.setCell(move, self.getMark()) 
            self.array.append(move)
       if move >=0 and move <=8 and board.getCell(move) == None:
            board.setCell(move, self.getMark()) 
            self.array.append(move)
            print(self.array)
       elif (board.getCell(move)!= None):  
             move = int(input("plese choose difference number:"))
             board.setCell(move, self.getMark()) 
             self.array.append(move)
     

class ComputerPlayer(Player):

    def makeRandonMoveIfComputerStart(self, board ):
        import random
        cellNumber = random.randint(0,8)
        board.setCell(cellNumber, self.getMark())
        return True

    def getDuplicate(self ,board):
        duplicate = []
        for i in Board.board:
            duplicate.append(i)
        return duplicate
    
    def checkForWinForComp(self,board ,mark):
        for i in range(0, 8): 
            copy = self.getDuplicate(board) 
            # print("board", board)
            # print("copy", copy)
            # print("i",i)
            if self.isSpaceFree(copy,i):
                if self.checkIfWin(copy):  
                    Board.board[i] = mark
                    return i, True
                else: 
                    return False
                    # self.currentGame = False
                    # return self.currentGame

    def checkForBlockThePlayer(self,board ,mark):
        for i in range(0, 8):
            copy = self.getDuplicate(board)
            if self.isSpaceFree(copy,i):
                self.setCopyCell(copy,i,mark)
                if self.checkIfWin(copy):
                 return i,
                else: self.RemoveCopyCell(copy,i)

            
    def isSpaceFree(self,board,move):
        return board[move] == None
    
    def makePlayerTurn(self,board):
        if self.checkForWinForComp(board,"O"):
           self.currentGame = False
           return self.currentGame
        else:
         while self.Hila:
           if self.checkForBlockThePlayer(board,"O"):
            self.Hila = False
           elif self.checkForCorners(board,"O"):
             self.Hila = False
           elif self.checkForSides(board,"O"):
             self.Hila = False
           elif self.checkForCenter(board,"0"):
             self.Hila = False
   
    def checkForCorners(self,board,mark):
        import random
        array = []
        for i in [0,2,6,8]:
            if Board.board[i] == None:
                array.append(i)
        x = (random.choice(array))
        self.setCell(x,mark)

    def checkForSides(self,board,mark):
        import random
        array = []
        for i in [1,3,5,7]:
            if Board.board[i] == None:
                array.append(i)
        x = (random.choice(array))
        self.setCell(x,mark)

    def checkForCenter(self,board,mark):
        if Board.board[4] == None:
            self.setCell(4,mark)
    
    def setCopyCell(self,copy,cellNumber,mark):
        copy[cellNumber] = mark

    def RemoveCopyCell(self,copy,cellNumber):
        copy[cellNumber] = None

    # def setCell(self, cellNumber, mark):
    #     self.board[cellNumber] = mark


    








    



# b1 = Board()
# b1.printBoard()
# p1 = HumanPlayer("Hila" , "X" , b1) 
# p2 = ComputerPlayer("comp" , "O" , b1) 

# p1.action(6)
# p2.action()
# b1.printBoard()
