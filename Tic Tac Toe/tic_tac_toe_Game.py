board=['_']*9
won=False
turn=0              # To know whose turn it is

#Function to Print the Board
def print_board():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])

#Function to Continously check for the Winner    
def check_winner():
    if board[0]==board[1]==board[2]=='X' or board[0]==board[1]==board[2]=='O':
        if board[0]=='O':
            return 1
        else:
            return 2
    elif board[3]==board[4]==board[5]=='X' or board[3]==board[4]==board[5]=='O':
        if board[3]=='O':
            return 1
        else:
            return 2
    elif board[6]==board[7]==board[8]=='X' or board[6]==board[7]==board[8]=='O':
        if board[6]=='O':
            return 1
        else:
            return 2
    elif board[0]==board[3]==board[6]=='X' or board[0]==board[3]==board[6]=='O':
        if board[0]=='O':
            return 1
        else:
            return 2
    elif board[1]==board[4]==board[7]=='X' or board[1]==board[4]==board[7]=='O':
        if board[1]=='O':
            return 1
        else:
            return 2
    elif board[2]==board[5]==board[8]=='X' or board[2]==board[5]==board[8]=='O':
        if board[2]=='O':
            return 1
        else:
            return 2
    elif board[0]==board[4]==board[8]=='X' or board[0]==board[4]==board[8]=='O':
        if board[0]=='O':
            return 1
        else:
            return 2
    elif board[2]==board[4]==board[6]=='X' or board[2]==board[4]==board[6]=='O':
        if board[2]=='O':
            return 1
        else:
            return 2
    else:
         return 0

print_board()
while not won and '_' in board:    
    pick_n=int(input("Pick a Number from 1 to 9:"))
    if pick_n in range(1,10) and board[pick_n-1]=='_':
        if turn%2==0:
            board[pick_n-1]='O'
            turn+=1
        else:
            board[pick_n-1]='X'
            turn+=1
    else:
        if board[pick_n-1]!='_':
            print("Already Filled..!!\n")
        else:
            print("Invalid Choice..(Pick between 1 to 9)\n")
    print_board()
    check_val=check_winner()   
    if check_val==1 or check_val==2:
        won=True
    
if check_val==1:
    print('\nPlayer with "O" won the Game')
elif check_val==2:
    print("\nPlayer with 'X' won the Game")
else:
    print("Match Over..!!\nNone of the Player won!!")
    
    




        