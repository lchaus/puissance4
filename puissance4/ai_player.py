from puissance4.board import Board
from puissance4.player import Player

class AI_player(Player):

    def __init__(self, name, symbol, board: Board):
        super().__init__(name, symbol, board)

    def play(self):
        #super().play()
        
        #No function game_over is defined(fill the whole board to fix)

        pass
        #column = input(f"{self.name}, in which column do you want to add your token ? ")
        #try:
        #    self.board.place(self.symbol, column)
        #except ValueError:
        #    print("Choose another column, this column is full ! ")
        #self.board.display() 
