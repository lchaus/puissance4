from puissance4.board import Board
from puissance4.player import Player
from puissance4.victory import Victory

def main():

    board = Board()
    flag = True

    name1 = str(input("Player 1, enter your name ?"))
    symbol1 = str(input("Player 1, enter your symbol (x or o) ?"))
    while symbol1 not in ('x', 'o'):
        symbol1 = str(input("Player 1, enter your symbol (x or o) ?"))

    name2 = str(input("Player 2, enter your name ?"))
    symbol2 = str(input("Player 2, enter your symbol (x or o) ?"))
    while symbol1 not in ('x', 'o') and symbol2 == symbol2:
        symbol1 = str(input("Player 2, enter your symbol (x or o) ?"))


    player1 = Player(name1, symbol1, board)
    player2 = Player(name2, symbol2, board)
    win = Victory(board.board)

    while flag:
        player1.play()
        win_check = win.check_victory(player1.symbol)
        print(player1.symbol)
        if win_check == True:
            flag = False
            print(f"{player1.name} wins the game !!!")
            break
        
        player2.play()
        win_check = win.check_victory(player2.symbol)
        if win_check == True:
            flag = False
            print(f"{player2.name} wins the game !!!")
            break
        
        #TODO : column index 0/1 mixed
        # 
    

    # victory = Victory(board)
    # victory.check_victory('x')
        
if __name__ == "__main__":
    main()

#play(input) takes a player (1 or 2) and a column -> goes into turn (in the beginning)
#turn(play) cahnges board[column][range(7)] while i in board[col][i] not ' ' ) ... set.cell
#           update board -> outputboard
#player() checks if victory and who
#main that gives rules and puts everything together
#placeholders !