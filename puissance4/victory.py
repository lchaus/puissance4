class Victory:


    def __init__(self, board):
        self.board = board   

    def check_victory(self, symbol):

        for row in range(7):
            if self._check_line(self.board[row],symbol) == True:
                return True
            
        for col in range(8):
            column = [self.board[row][col] for row in range(7)]
            if self._check_line(column,symbol) == True:
                return True
    
        for row in range(7):
            for col in range(8):
                if (self._check_line(self.board[row][col],symbol) == symbol 
                    and self._check_line(self.board[row+1][col+1],symbol) == symbol
                    and self._check_line(self.board[row+2][col+2],symbol) == symbol
                    and self._check_line(self.board[row+3][col+3],symbol) == symbol):
                    return True
        return False
    
    def _check_line(self, line, symbol):
        count = 0
        for cell in line:
            if cell == symbol:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False