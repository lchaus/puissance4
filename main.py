from puissance4.board import Board
from puissance4.player import Player

def main():

    board = Board()
    flag = True

    name1 = str(input("Player 1, enter your name ?"))
    symbol1 = str(input("Player 1, enter your symbol (x or o) ?"))
    name2 = str(input("Player 1, enter your name ?"))
    symbol2 = str(input("Player 1, enter your symbol (x or o) ?"))

    player1 = Player(name1, symbol1, board)
    player2 = Player(name2, symbol2, board)

    while flag:
        player1.play()
        player2.play()
        #if player1.wins():
        #    flag = false
        # yay !
        
        #TODO : column index 0/1 mixed 
        #
if __name__ == "__main__":
    main()

#play(input) takes a player (1 or 2) and a column -> goes into turn (in the beginning)
#turn(play) cahnges board[column][range(7)] while i in board[col][i] not ' ' ) ... set.cell
#           update board -> outputboard
#player() checks if victory and who
#main that gives rules and puts everything together
#placeholders !