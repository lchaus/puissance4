class Board:
    def __init__(self):
        self.board = [['   ' for _ in range(7)] for _ in range(7)]  

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
        if column < 0 or column > 6:
            raise IndexError('Column must be between 1 and 7')

        for row in range(6, -1, -1):
            if self.board[row][column] == '   ':
                self.board[row][column] = f' {symbol} '
                return
        raise ValueError('full')
    
    
    def get_valid_moves(self):
        return [col for col in range(8) if self.board[0][col] == '   ']

    def is_full(self):
        return all(self.board[0][col] != '   ' for col in range(8))

    
    def display(self):
        cell = ''
        for row in self.board:
            cell += '+---'*7 + '+' + '\n' + '|'+ '|'.join(row) + '|' +'\n'
        cell += '+---'*7 + '+' + '\n' 
        print(cell)