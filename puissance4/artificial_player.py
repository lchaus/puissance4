from puissance4.board import Board
from puissance4.player import Player

class AI_player(Player):

    def __init__(self, name, symbol, board: Board):
        super().__init__(name, symbol, board)
        print(symbol)

    def play(self):
        #super().play()
        pass