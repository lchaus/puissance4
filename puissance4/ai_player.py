from puissance4.board import Board
from puissance4.player import Player
from puissance4.victory import Victory
from icecream import ic

import copy

class AI_player(Player):

    def __init__(self, name, symbol, board: Board, depth=2):
        super().__init__(name, symbol, board)
        self.depth = depth
    
    def play(self):
        available_moves = {}
        for move in range(6):
            score = self.minmax(move, self.symbol, depth=self.depth)
            available_moves[move] = score

        bestmoves = sorted(available_moves, key=available_moves.get)
        flag = True
        cpt = 0
        while flag:  
            try:
                self.board.place(self.symbol, bestmoves[cpt])
                flag = False
            except ValueError:
                cpt += 1
                pass

        self.board.display() 

    def minmax(self, move, symbol, depth):
        bestscore = 0
        bestmove = 0
        noeud = 0
        score =  0
        
        vic_ob = Victory(self.board.board)

        if (not super().can_play()) or (depth == 0):
            bestscore = vic_ob.check_move(self.symbol)
            return bestscore

        #MAX
        if (noeud % 2) == 0:
            bestscore = -10000
            for column in range(6):
                try:
                    board_copy = copy.deepcopy(self.board.board)
                    self.board.place(self.symbol, column)
                    score = self.minmax(column, self.symbol, depth = depth-1)
                    self.board.board = board_copy
                    if score > bestscore:
                        bestscore = score
                        bestmove = column
                except ValueError:
                    continue
            noeud += 1
            depth -= 1 

        #MIN
        elif (noeud % 2) == 1:
            bestscore = +10000
            for column in range(6):
                try:
                    board_copy = copy.deepcopy(self.board.board)
                    #Play for other player
                    other_symbol = "".join({"x","o"} - set(self.symbol))
                    self.board.place(other_symbol, column)
                    score = self.minmax(column, other_symbol, depth = depth-1)
                    self.board.board = board_copy
                    noeud += 1
                    depth -= 1 
                    if score < bestscore: 
                        bestscore = score
                        bestmove = column
                except ValueError:
                    continue
            noeud += 1
            depth -= 1 

        return bestscore


               
            

            

