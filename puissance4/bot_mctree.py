import random
import math
from copy import deepcopy
from board import Board
from victory import Victory

class MCtreeNode:

    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.children = []
        self.wins = 0
        self.visits = 0
        self.untried_moves = board.get_valid_moves()


    def select_child(self):
        best_child = None
        best_value = - 0.01
        for child in self.children:
            ucb1_value = (child.wins / child.visits) + math.sqrt(2 * math.log(self.visits) / child.visits)
            if ucb1_value > best_value:
                best_value = ucb1_value
                best_child = child
        return best_child
    
    def expand(self):
        move = self.untried_moves.pop()
        new_board = deepcopy(self.board)
        new_board.play('x' if new_board.get_valid_moves().count() % 2 == 0 else 'o', move)
        child_node = MCtreeNode(new_board, parent=self, move=move)
        self.children.append(child_node)
        return child_node
    
    def simulate(self):
        current_board = deepcopy(self.board)
        current_symbol = 'x' if current_board.get_valid_moves().count() % 2 == 0 else 'o'
        while current_board.get_winner() is None:
            valid_moves = current_board.get_valid_moves()
            move = random.choice(valid_moves)
            current_board.place(current_symbol, move)
            current_symbol = 'o' if current_symbol == 'x' else 'x'
        winner = current_board.get_winner()
        if winner == 'x':
            return 1
        elif winner == 'o':
            return -1
        else:
            return 0
    
    def backpropagate(self, result):
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(result)

class MCTS:

    def __init__(self, root):
        self.root = root
    
    def run(self, iterations=1000):
        for _ in range(iterations):
            node = self.root
            # Selection
            while node.untried_moves == [] and node.children != []:
                node = node.select_child()
            # Expansion
            if node.untried_moves != []:
                node = node.expand()
            # Simulation
            result = node.simulate()
            # Backpropagation
            node.backpropagate(result)
        # Return the move with the most visits
        best_move = None
        best_visits = -float('inf')
        for child in self.root.children:
            if child.visits > best_visits:
                best_visits = child.visits
                best_move = child.move
        return best_move