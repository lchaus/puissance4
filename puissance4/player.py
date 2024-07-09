from puissance4.board import Board

class Player():
    def __init__(self, name, symbol, board : Board):
        self.name = name
        self.symbol = symbol
        self.board = board
    
    def play(self):
        column = int(input(f"{self.name}, in which column do you want to add your token ?"))
        try:
            self.board.place(self.symbol, column)
        except ValueError:
            print("Choose another column, this column is full")
        self.board.display() 
