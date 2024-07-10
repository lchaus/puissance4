class Board:
    def __init__(self):
        self.board = [['   ' for _ in range(8)] for _ in range(7)]  

    def place(self,symbol,column):
        flag = True
        while flag:
            try:
                column = int(column)
                flag = False
            except ValueError:
                column = input("Column must be an integer ! Try again :")
                
        if symbol not in ('x', 'o'):
            raise ValueError('Symbol must be "x" or "o"')
        if column < 0 or column > 7:
            raise ValueError('Column must be between 1 and 7')

        for row in range(6, -1, -1):
            if self.board[row][column] == '   ':
                self.board[row][column] = f' {symbol} '
                return
        raise ValueError('full')
    
    def display(self):
        cell = ''
        for row in self.board:
            cell += '+---'*7 + '+' + '\n' + '|'+ '|'.join(row) +'\n'
        print(cell)

#import copy
#
#class Board():
#
#    def __init__(self):
#        boardr = [' ' for i in range(7)]
#        self.board = [copy.deepcopy(boardr) for i in range(6)]
#    
#    def display(self):
#        print(f"+ - - - + - - - + - - - + - - - + - - - + - - - + - - - +")
#        print(f"|   {self.board[0][0]}   |   {self.board[0][1]}   |   {self.board[0][2]}   |   {self.board[0][3]}   |   {self.board[0][4]}   |   {self.board[0][5]}   |   {self.board[0][6]}   |")
#        print(f"+ - - - + - - - + - - - + - - - + - - - + - - - + - - - +")
#        print(f"|   {self.board[1][0]}   |   {self.board[1][1]}   |   {self.board[1][2]}   |   {self.board[1][3]}   |   {self.board[1][4]}   |   {self.board[1][5]}   |   {self.board[1][6]}   |")
#        print(f"+ - - - + - - - + - - - + - - - + - - - + - - - + - - - +")
#        print(f"|   {self.board[2][0]}   |   {self.board[2][1]}   |   {self.board[2][2]}   |   {self.board[2][3]}   |   {self.board[2][4]}   |   {self.board[2][5]}   |   {self.board[2][6]}   |")
#        print(f"+ - - - + - - - + - - - + - - - + - - - + - - - + - - - +")
#        print(f"|   {self.board[3][0]}   |   {self.board[3][1]}   |   {self.board[3][2]}   |   {self.board[3][3]}   |   {self.board[3][4]}   |   {self.board[3][5]}   |   {self.board[3][6]}   |")
#        print(f"+ - - - + - - - + - - - + - - - + - - - + - - - + - - - +")
#        print(f"|   {self.board[4][0]}   |   {self.board[4][1]}   |   {self.board[4][2]}   |   {self.board[4][3]}   |   {self.board[4][4]}   |   {self.board[4][5]}   |   {self.board[4][6]}   |")
#        print(f"+ - - - + - - - + - - - + - - - + - - - + - - - + - - - +")
#        print(f"|   {self.board[5][0]}   |   {self.board[5][1]}   |   {self.board[5][2]}   |   {self.board[5][3]}   |   {self.board[5][4]}   |   {self.board[5][5]}   |   {self.board[5][6]}   |")
#        print(f"+ - - - + - - - + - - - + - - - + - - - + - - - + - - - +")
#
#    def set_cell(self):
#        pass