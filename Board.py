class Board:

    boardArray =  [None, None, None, None, None, None, None, None, None]

    def __init__(self,board):
        self.boardArray = board

    def setCell(self, cellNumber, mark):
        self.boardArray[cellNumber] = mark
    
    def getCell(self, cellNumber):
        try:
            return self.boardArray[cellNumber] 
        except:
            print("Not a valid cell")
            return False

    def setBoard(self,board):
        self.boardArray = board

    def getBoard(self):
        return self.boardArray[:] 

    def checkIfWin(self):
           return self.checkRow() or self.checkDiagonal() or self.checkCol()

    def checkRow(self):
        if self.boardArray[0] == self.boardArray[1] == self.boardArray[2] and self.boardArray[0] != None:
            return True
        elif self.boardArray[3] == self.boardArray[4] == self.boardArray[5] and self.boardArray[3] != None:
            return True
        elif self.boardArray[6] == self.boardArray[7] == self.boardArray[8] and self.boardArray[6] != None:
            return True

    def checkDiagonal(self):
        if self.boardArray[0] == self.boardArray[4] == self.boardArray[8] and self.boardArray[0] != None:
            return True
        elif self.boardArray[2] == self.boardArray[4] == self.boardArray[6] and self.boardArray[4] != None:
            return True

    def checkIfTie(self):
        return None not in self.boardArray

    def checkCol(self):
        if self.boardArray[0] == self.boardArray[3] == self.boardArray[6] and self.boardArray[0] != None:
            return True
        elif self.boardArray[1] == self.boardArray[4] == self.boardArray[7] and self.boardArray[1] != None:
            return True
        elif self.boardArray[2] == self.boardArray[5] == self.boardArray[8] and self.boardArray[2] != None:
            return True

    def printboardArray(self):
        def normalizeCell(cell):
            return cell if cell is not None else ' '
        print(normalizeCell(self.boardArray[0]) + '|' + normalizeCell(self.boardArray[1]) + '|' + normalizeCell(self.boardArray[2]))
        print('-+-+-')
        print(normalizeCell(self.boardArray[3])+ '|' + normalizeCell(self.boardArray[4]) + '|' + normalizeCell(self.boardArray[5]))
        print('-+-+-')
        print(normalizeCell(self.boardArray[6]) + '|' + normalizeCell(self.boardArray[7]) + '|' + normalizeCell(self.boardArray[8]))
        print("")
        print("")

