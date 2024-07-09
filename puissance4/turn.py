from board import Board

class Turn:

    def __init__(self):
        self.board = [['   ' for _ in range(8)] for _ in range(7)]  

    def place(self,symbol,column):
        if symbol not in ('x', 'o'):
            raise ValueError('must be "x" or "o"')
        if column < 1 or column > 7:
            raise ValueError('must be between 1 and 7')

            
        for row in range(6, -1, -1):
            if self.board[row][column] == '   ':
                self.board[row][column] = f' {symbol} '
                return
        raise ValueError('full')
    
    def __str__(self):

        cell = ''
        for row in self.board:
            cell += '+---'*7 + '+' + '\n' + '|'+ '|'.join(row) +'\n'
        return cell

  
turn = Turn()

turn.place('x',3)
turn.place('o',5)
turn.place('x',3)
print(turn)