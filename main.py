from puissance4.board import Board

def main() :

    board = Board()
    board.display()
    

if __name__ == "__main__":
    main()

#play(input) takes a player (1 or 2) and a column -> goes into turn (in the beginning)
#turn(play) cahnges board[column][range(7)] while i in board[col][i] not ' ' ) ... set.cell
#           update board -> outputboard
#player() checks if victory and who
#main that gives rules and puts everything together
#placeholders !