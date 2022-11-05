class Board:
    board =  [None, None, None, None, None, None, None, None, None]
   
    def setCell(self, cellNumber, mark):
        self.board[cellNumber] = mark
    
    def getCell(self, cellNumber):
       return self.board[cellNumber] 
    def checkIfWin(self):
           return self.checkRow() or self.checkDiagonal() or self.checkCol()

    def checkCol(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != None:
            return True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != None:
            return True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != None:
            return True

    def checkDiagonal(self):
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != None:
            return True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[4] != None:
            return True

    def checkIfTie(self):
        return None not in self.board

    def checkRow(self):
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != None:
            return True
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != None:
            return True
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != None:
            return True

    def printBoard(self):
        def normalizeCell(cell):
            return cell if cell is not None else ' '
        print(normalizeCell(self.board[0]) + '|' + normalizeCell(self.board[1]) + '|' + normalizeCell(self.board[2]))
        print('-+-+-')
        print(normalizeCell(self.board[3])+ '|' + normalizeCell(self.board[4]) + '|' + normalizeCell(self.board[5]))
        print('-+-+-')
        print(normalizeCell(self.board[6]) + '|' + normalizeCell(self.board[7]) + '|' + normalizeCell(self.board[8]))