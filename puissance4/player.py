import copy
#from icecream import ic
from puissance4.board import Board

class Player():
    def __init__(self, name, symbol, board : Board):
        self.name = name
        self.symbol = symbol
        self.board = board
    
    def play(self):
        column = input(f"{self.name}, in which column do you want to add your token ? ")
        try:
            self.board.place(self.symbol, column)
        except ValueError:
            print("Choose another column, this column is full ! ")
            self.play()
        except IndexError:
            print("Column must be between 0-6! Try again :")
            self.play()

        self.board.display() 


    def can_play(self):
        test_board = copy.deepcopy(self.board.board)
        can_play = True
        row_full = 0
        for row in test_board:
            if '   ' not in set(row):
                row_full += 1
        if row_full == 7:
            can_play = False 
        return can_play 
        