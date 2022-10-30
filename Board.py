class Board:
   __board =  [None, None, None, None, None, None, None, None, None]
   
   def setCell(self, cellNumber, mark):
        self.__board[cellNumber] = mark
    
   def getCell(self, cellNumber):
       return self.__board[cellNumber] 

   def checkIfWin(self):
    return self.checkRow() or self.checkDiagonal() or self.checkCol()

   def checkCol(self):
        if self.__board[0] == self.__board[1] == self.__board[2] and self.__board[0] != None:
            return True
        elif self.__board[3] == self.__board[4] == self.__board[5] and self.__board[3] != None:
            return True
        elif self.__board[6] == self.__board[7] == self.__board[8] and self.__board[6] != None:
            return True

   def checkDiagonal(self):
        if self.__board[0] == self.__board[4] == self.__board[8] and self.__board[0] != None:
            return True
        elif self.__board[2] == self.__board[4] == self.__board[6] and self.__board[4] != None:
            return True

   def checkIfTie(self):
        return None not in self.__board

   def checkRow(self):
        if self.__board[0] == self.__board[3] == self.__board[6] and self.__board[0] != None:
            return True
        elif self.__board[1] == self.__board[4] == self.__board[7] and self.__board[1] != None:
            return True
        elif self.__board[2] == self.__board[5] == self.__board[8] and self.__board[2] != None:
            return True

   def printBoard(self):
    def normalizeCell(cell):
        return cell if cell is not None else ' '
    print(normalizeCell(self.__board[0]) + '|' + normalizeCell(self.__board[1]) + '|' + normalizeCell(self.__board[2]))
    print('-+-+-')
    print(normalizeCell(self.__board[3])+ '|' + normalizeCell(self.__board[4]) + '|' + normalizeCell(self.__board[5]))
    print('-+-+-')
    print(normalizeCell(self.__board[6]) + '|' + normalizeCell(self.__board[7]) + '|' + normalizeCell(self.__board[8]))

   


 
