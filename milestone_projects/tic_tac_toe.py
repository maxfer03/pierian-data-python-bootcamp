from random import randint
import re

#here the board values are stored
bv = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' '],
]

def draw_board():
    global bv
    print(
        f"""
            1   2   3  
        A   {bv[0][0]} | {bv[0][1]} | {bv[0][2]}  
           ---|---|--- 
        B   {bv[1][0]} | {bv[1][1]} | {bv[1][2]}
           ---|---|--- 
        C   {bv[2][0]} | {bv[2][1]} | {bv[2][2]}    
        """
    )


def format_input(list):
    new_list = [list[0],int(list[1])-1]
    if   list[0] == 'a': new_list[0] = 0
    elif list[0] == 'b': new_list[0] = 1
    elif list[0] == 'c': new_list[0] = 2

    if int(list[1]) <= 0 or int(list[1]) > 3:
        raise ValueError("wrong num")




    return new_list

def validate_xy(xy):
    global bv
    if bv[xy[0]][xy[1]] == ' ':
        return True
    else:
        return False

def check_winner(xo):
    global bv
    col_1 = [bv[0][0],bv[1][0],bv[2][0]]
    col_2 = [bv[0][1],bv[1][1],bv[2][1]]
    col_3 = [bv[0][2],bv[1][2],bv[2][2]]

    diag_1 = [bv[0][0],bv[1][1],bv[2][2]]
    diag_2 = [bv[0][2],bv[1][1],bv[2][0]]
    

    #check rows
    if bv[0] == [xo,xo,xo] \
    or bv[1] == [xo,xo,xo] \
    or bv[2] == [xo,xo,xo]:
        return True
    #check columns
    elif col_1 == [xo,xo,xo] \
    or col_2 == [xo,xo,xo] \
    or col_3 == [xo,xo,xo]: 
        return True
    #check diagonals
    elif diag_1 == [xo,xo,xo] \
    or diag_2 == [xo,xo,xo]:
        return True
    else:
        return False


def result(xo):
    global bv
    filled_counter = 0
    result = check_winner(xo)
    for row in bv:
        for col in row:
            if col != ' ':
                filled_counter+=1
    
    if result:
        print(f'{xo} wins!')
        return True
    elif result != True and filled_counter == 9:
        print('tie!')
        return True




## Game loop

print("--- Tick Tack Toe ---")

draw_board()

print("You are the x\n")

while True:
    
   
    while True:
        user_row = input('Select row: ')
        user_col = input('Select column: ')
        try:
            user_input = format_input([user_row.lower(), user_col])
        except: 
            draw_board()
            print("Column must be a, b or c.")
            print("Row must be 1, 2 or 3\n")
            continue

        if validate_xy(user_input):
            bv[user_input[0]][user_input[1]] = 'x'
            break
        else: 
            print('place taken!')
            
    draw_board()

    if result('x'):
        break
    
    next_t = input('press enter to continue')

    while True:
        num = [randint(0,2),randint(0,2)]
        if validate_xy(num):
            bv[num[0]][num[1]] = 'o'
            break
        else: 
            continue

    draw_board()

    if result('o'):
        break