from puissance4.board import Board
from functools import partial
from icecream import ic

class Victory:

    def __init__(self, board):
        self.board = board  

    def victory_kernel(self, i, j):
        kernel = []
        for row in range(i, i+4):
            kernel.append([elt.strip(" ") for elt in self.board[row][j-4:j]])
        return kernel
        
    def check_kernel(self, kernel, symbol):
        #Check rows
        for row in kernel:
            if set(row) == set(symbol):
                return True

        #Check columns
        for i in range(4):
            column = [row[i] for row in kernel]
            if set(column) == set(symbol):
                return True

        #Check diagonals
        diag1 = [kernel[i][-(i+1)] for i in range(len(kernel))]
        diag2 = [kernel[i][i] for i in range(len(kernel))]

        if set(diag1) == set(symbol):
            return True
        elif set(diag2) == set(symbol):
            return True
        else:
            return False
    
    def check_vector(self, vector, symbol):
        '''Check the return score of a given vector of the kernel'''
        twos = 50
        threes = 500
        fours = 4000
        score = 0
        cpt = 0

        for elt in vector:
            if elt == symbol:
                cpt += 1
        if cpt == 2:
            score += twos
        elif cpt == 3:
            score += threes
        elif cpt == 4:
            score += fours

        return score
    
    def check_score_kernel(self, kernel, symbol):
        """ Alternatively, check the 'score' of a kernel, associated with number of 2, 3, or 4 symbols in a row """
        score = 0
        
        #Check rows
        for row in kernel:
            ic(row, symbol)
            score += self.check_vector(row, symbol)

        #Check columns
        for i in range(4):
            column = [row[i] for row in kernel]
            score += self.check_vector(column, symbol)

        #Check diagonals
        diag1 = [kernel[i][-(i+1)] for i in range(len(kernel))]
        score += self.check_vector(diag1, symbol)

        diag2 = [kernel[i][i] for i in range(len(kernel))]
        score += self.check_vector(diag2, symbol)

        return score
 

    def check_move(self, symbol):
        score = 0
        for i in range(4):
            for j in range(4,8):
                #Lots of useless computations here (change stride of kernel)
                ker = self.victory_kernel(i, j)
                score += self.check_score_kernel(ker, symbol)
        return score



    def check_victory(self, symbol):
        win = False
        for i in range(4):
            for j in range(4,8):
                ker = self.victory_kernel(i, j)
                win = self.check_kernel(ker, symbol)
                if win:
                    return True
        return win
    
    def get_winner(self):
        victory = Victory(self.board)
        if victory.check_victory('x'):
            return 'x'
        elif victory.check_victory('o'):
            return 'o'
        elif self.is_full():
            return 'draw'
        else:
            return None

#    def check_victory(self, symbol):
#         
#        for row in range(7):
#            ic(self.board[row], row)
#            if self._check_line(self.board[row],symbol) == True:
#                return True
#            
#        for col in range(8):
#            column = [self.board[row][col] for row in range(7)]
#            ic(column, col)
#            if self._check_line(column,symbol) == True:
#                return True
#    
#        for row in range(7):
#            for col in range(8):
#                ic(self._check_line(self.board[row][col],symbol) == symbol)
#                if (self._check_line(self.board[row][col],symbol) == symbol 
#                    and self._check_line(self.board[row+1][col+1],symbol) == symbol
#                    and self._check_line(self.board[row+2][col+2],symbol) == symbol
#                    and self._check_line(self.board[row+3][col+3],symbol) == symbol):
#                    return True
#        return False
#    
#    def _check_line(self, line, symbol):
#        count = 0
#        for cell in line:
#            if cell.strip(" ") == symbol:
#                count += 1
#                if count == 4:
#                    return True
#            else:
#                count = 0
#        return False

#myboard = Board()
#ic(myboard.board)
#win = Victory(myboard.board)
#
#
#myboard.place("x", 1)
#myboard.place("o", 2)
#myboard.place("o", 3)
#myboard.place("x", 1)
#myboard.place("o", 3)
#myboard.place("x", 3)
#myboard.place("o", 4)
#myboard.place("x", 4)
#myboard.place("o", 4)
#myboard.place("o", 4)
#myboard.place("o", 5)
#
#
#ic(myboard.board)
#print(win.check_victory('x'))
#print(win.check_victory('o'))
#
##ker = win.victory_kernel(3,4)
##win.check_kernel(ker, "x")
#myboard.display()