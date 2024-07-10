from puissance4.board import Board
from puissance4.player import Player
import copy

class AI_player(Player):

    def __init__(self, name, symbol, board: Board, depth=2):
        super().__init__(name, symbol, board)
        self.depth = depth

    def play(self):

        self.minmax(depth=self.depth)
        self.board.display() 

    def minmax(self, depth = 2):
        bestscore = 0
        bestmove = 0
        noeud = 0
        score =  0

        if super.can_play() or depth == 0:
            return bestmove
        #MAX
        if noeud == 3:
            bestscore = -10000
            for column in range(6):
                virtual_board = copy.deepcopy(self.board.board)
                self.board.place(self.symbol, column)
                score = self.minmax(depth = depth-1)
                self.board.board = virtual_board

                if score > bestscore:
                    bestscore = score
                    bestmove = column
        #MIN
        else:
            pass


               
            

            

