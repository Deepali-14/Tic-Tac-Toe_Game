#Tic-Tac-Toe Game
#Deepali



board=["   " for i in range(9)]     #declaring board(a [3*3] matrix)



def print_board():      #to print board     
    row1="| {} | {} | {} |".format(board[0], board[1], board[2])
    row2="| {} | {} | {} |".format(board[3], board[4], board[5])
    row3="| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()



def is_victory(icon):   #to check victory condition(which is true for 3 rows, 3 columns and 2 diagonals)
    if (board[0]==icon and board[1]==icon and board[2]==icon) or \
       (board[3]==icon and board[4]==icon and board[5]==icon) or \
       (board[6]==icon and board[7]==icon and board[8]==icon) or \
       (board[0]==icon and board[3]==icon and board[6]==icon) or \
       (board[1]==icon and board[4]==icon and board[7]==icon) or \
       (board[2]==icon and board[5]==icon and board[8]==icon) or \
       (board[0]==icon and board[4]==icon and board[8]==icon) or \
       (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    
    else:
        return False



def player_move(icon):   #to move the game player wise
    if icon == "X":
        number=1
        
    elif icon == "O":
        number=2
        
    print("Your turn player {}({})!".format(number,icon))

    choice=int(input("Enter your move (1-9): ").strip())
    
    if board[choice - 1]=="   ":
        board[choice - 1 ]=icon
        
    else:    #if the position is invalid, give that player a second chance
        print()
        print("Oops! That space is occupied! Try again!")
        print()
        player_move(icon)



def is_draw():   #to check for draw condition which happens only when there is no space on the board
    if "   " not in board:
        return True
    
    else:
        return False



while True:     #game control where the control flow only ends if either one wins or match draws
    print_board()
    player_move("X")
    print_board()
    
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    
    elif is_draw():
        print("Oops! It is a draw!")
        break
    
    player_move("O")
    
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations!")
        break
