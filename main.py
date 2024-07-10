from puissance4.board import Board
from puissance4.player import Player
from puissance4.victory import Victory
from puissance4.artificial_player import AI_player

def main():

    board = Board()
    flag = True
    
    nb = int(input("Number of players ? (1 or 2)\n"))

    if nb == 2:
        name1 = str(input("Player 1, enter your name ?\n"))
        symbol1 = str(input("Player 1, enter your symbol (x or o) ?\n"))
        while symbol1 not in ('x', 'o'):
            symbol1 = str(input("Player 1, enter your symbol (x or o) ?\n"))

        name2 = str(input("Player 2, enter your name ?\n"))
        symbol2 = str(input("Player 2, enter your symbol (x or o) ?\n"))

        while symbol2 not in ('x', 'o') or symbol2 == symbol1:
            symbol2 = str(input(f"Player 2, enter your symbol (x or o) and different from {name1}?\n"))

        player1 = Player(name1, symbol1, board)
        player2 = Player(name2, symbol2, board)

    elif nb == 1:
        name1 = str(input("Player 1, enter your name ?\n"))
        symbol1 = str(input("Player 1, enter your symbol (x or o) ?\n"))
        while symbol1 not in ('x', 'o'):
            symbol1 = str(input("Player 1, enter your symbol (x or o) ?\n"))
        player1 = Player(name1, symbol1, board)
        player2 = AI_player("C3PO", "".join({"x","o"} - set(symbol1)), board)
        

    win = Victory(board.board)

    while flag:
        if player1.can_play():
            player1.play()
            win_check = win.check_victory(player1.symbol)
            if win_check == True:
                flag = False
                print(f"{player1.name} wins the game !!!\n")
                break
        if player2.can_play(): 
            player2.play()
            win_check = win.check_victory(player2.symbol)
            if win_check == True:
                flag = False
                print(f"{player2.name} wins the game !!!\n")
                break
        if (not player1.can_play()) and (not player2.can_play()):
            print("The board is full ! Every one loses!")
            break

        
if __name__ == "__main__":
    main()

#play(input) takes a player (1 or 2) and a column -> goes into turn (in the beginning)
#turn(play) cahnges board[column][range(7)] while i in board[col][i] not ' ' ) ... set.cell
#           update board -> outputboard
#player() checks if victory and who
#main that gives rules and puts everything together
#placeholders !