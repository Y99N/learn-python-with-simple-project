import random

board = ["1","2","3","4","5","6","7","8","9"]
players = ["p1","p2"]
#display the play board
def display_board():
    print("--------------")
    print(" | "+board[0]+" | "+board[1]+" | "+board[2]+" | ")
    print("--------------")
    print(" | "+board[3]+" | "+board[4]+" | "+board[5]+" | ")
    print("--------------")
    print(" | "+board[6]+" | "+board[7]+" | "+board[8]+" | ")
    print("--------------")
#ask player to choose a position and check if it's available
def choose_position(person):
    a = int(input(person+" Enter your position  "))
    while a-1 > 9 or a-1 < 0:
        print("No such position  ")
        a = int(input(person+" Enter your position  "))
    while board[a-1] == "X" or board[a-1] == "O":
        print("Position all ready token  ")
        a = int(input(person+" Enter your position  "))
        break
    return a
#return False in case there is a winner after that the player choose his position on the board
def __check__(x_o):
    if board[0] == board[1] == board[2] == x_o or board[3] == board[4] == board[5] == x_o or board[6] == board[7] == board[8] == x_o:
        return False
    elif board[0] == board[3] == board[6] == x_o or board[1] == board[4] == board[7] == x_o or board[2] == board[5] == board[8] == x_o:
        return False
    elif board[0] == board[4] == board[8] == x_o or board[2] == board[4] == board[6] == x_o:
        return False
    else:
        return True
    
def game_play():
    display_board()
    #enter players name
    p1 = input("player 1 name: ")
    p2 = input("player 2 name: ")
    choie_1_or_2 = [p1 , p2]
    #choose randomly the first player who will play
    first = random.choice(choie_1_or_2)
    if p1 == first:
        sec = p2
    else:
        sec = p1
    print(first+" you will play fisrt, then "+sec+" you will play second")
    choie_x_or_o=['x','o']
    #choose the element that the first player wanna use, 'X or 'O', then give the secound player the other element to play with
    c1 = input(first+" do you wanna play with X or O : ").lower()
    while c1 not in choie_x_or_o:
        print("no available coice")
        c1 = input(first+" do you wanna play with X or O : ").lower()
    if c1 == 'x':
        c2 = 'o'
    else:
        c2='x'
    print(first+" you choose '"+c1.upper()+"' , "+sec+" you will play with '"+c2.upper()+"' ")  
    C1 = c1.upper()
    C2 = c2.upper()
    star = True
    while star == True:
        i = choose_position(first)
        #replace in the board the element that the first player choose in the position that he choose
        board[i-1]=C1
        display_board()
        if __check__(C1) == False:
            print(first+" you win")
            star = False
        else:
            star = True
        ii = choose_position(sec)
        #replace in the board the element of the secound player choose in the position that he choose
        board[ii -1]=C2
        display_board()
        if __check__(C2) == False:
            print(sec+" you win")
            star = False
        else:
            star = True


#game start
game_play()
