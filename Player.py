from Board import Board 
# from Enums import Mark
class Player:
    move = ""
    array = []

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

    def isSpaceFree(self, board ,move):
        pass

    def getDuplicate(self, board):
        pass

    # def getDuplicate(self,board):
    #     pass
        
class HumanPlayer(Player):
    def makeRandonMoveIfComputerStart(self, board):
        return False
    
    def makePlayerTurn(self, board):
        # self.move = int(input(f"player:" + {self.currPlayer.name} +  "please enter number between 0-8 "))
       move = int(input(f"player please enter number between 0-8 "))
       print(move)
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

    def getDuplicate(self, board):
        duplicate = []
        print("board",self.board)
        for i in self.board:
            duplicate.append(i)
        return duplicate
    
    def checkForWinForComp(self,board ,mark):
        for i in range(0, 8):
            copy = self.getDuplicate(board)
            if self.isSpaceFree(copy, i):
                self.setCell(i ,mark)
                if self.checkIfWin(copy, mark):
                 return i

    def checkForBlockThePlayer(self,board ,mark):
        for i in range(0, 8):
            copy = self.getDuplicate(board)
            if self.isSpaceFree(copy, i):
                self.setCell(i ,mark)
                if self.checkIfWin(copy, mark):
                 return i
            
    def isSpaceFree(board, move):
       return board[move] == None
    
    def makePlayerTurn(self,board):
        self.checkForWinForComp(board,"O")
        self.checkForBlockThePlayer(board, "O")
        self.checkForCorners(board)
        self.checkForSides(board)
        self.checkForCenter(board)

    def checkForCorners(self, board,mark):
        import random
        array = []
        for i in [0,2,6,8]:
            if board[i] == None:
                array.append(i)
        x = (random.choice(array))
        self.setCell(x,mark)

    def checkForSides(self, board,mark):
        import random
        array = []
        for i in [1,3,5,7]:
            if board[i] == None:
                array.append(i)
        x = (random.choice(array))
        self.setCell(x,mark)

    def checkForCenter(self,board,mark):
        if board[4] == None:
            self.setCell(4,mark)


    








    



# b1 = Board()
# b1.printBoard()
# p1 = HumanPlayer("Hila" , "X" , b1) 
# p2 = ComputerPlayer("comp" , "O" , b1) 

# p1.action(6)
# p2.action()
# b1.printBoard()
