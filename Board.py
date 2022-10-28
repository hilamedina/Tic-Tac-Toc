class Board:
   board = ['','','','','','','','',''] 

   def printBoard(self):
        print(self.board[0] ' | ' + self.board[1] + '| ' + self.board[2])
        print('-+-+-')
        print(self.board[3] + ' | ' + self.board[4] + '|' + self.board[5])
        print('-+-+-')
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])
       
xoBoard = Board()
xoBoard.printBoard()
# self.board[0] if self.board[0] is not None else ' '