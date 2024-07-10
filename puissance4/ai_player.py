from puissance4.board import Board
from puissance4.player import Player

class AI_player(Player):

    def __init__(self, name, symbol, board: Board, depth=2):
        super().__init__(name, symbol, board)
        self.depth = depth

    def play(self):

        self.minmax(depth=self.depth)
        self.board.display() 

    def minmax(self, depth = 2):
        if super.can_play() or depth == 0:


