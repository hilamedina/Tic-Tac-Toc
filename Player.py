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

    def makeRandonMoveIfComputerStart(self):
        pass

    def makePlayerTurn(self, board):
        pass
        
class HumanPlayer(Player):
    def makeRandonMoveIfComputerStart(self, board):
        return False
    
    def makePlayerTurn(self, board):
        # self.move = int(input(f"player:" + {self.currPlayer.name} +  "please enter number between 0-8 "))
       move = int(input(f"player please enter number between 0-8 "))
       if move >=0 and move <=8 and board.getCell(move) == None:
            board.setCell(move, self.getMark()) 

class ComputerPlayer(Player):
    def makeRandonMoveIfComputerStart(self, board):
        import random
        cellNumber = random.randint(0,8)
        board.setCell(cellNumber, self.getMark())
        return True

    def makePlayerTurn(self, board):
        # TODO
        pass


# b1 = Board()
# b1.printBoard()
# p1 = HumanPlayer("Hila" , "X" , b1) 
# p2 = ComputerPlayer("comp" , "O" , b1) 

# p1.action(6)
# p2.action()
# b1.printBoard()


  