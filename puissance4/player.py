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
        except IndexError:
            print("Column must be between 0-6! Try again :")

        self.board.display() 
