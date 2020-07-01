import time

#INITIALIZATION
win = False
tie = False
checkWin = False #if it is true, that means there is a win
player = 1
letter = "X"
moves = 1

def createBoard():
    board =[["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"]]
    return board

def drawBoard(board):
    print("0 1 2 3 4 5 6") 
    print("=============")
    for x in range(6):      #connect four boards are 7x6
        for y in range(7):
            print(board[y][x] + " ", end = '')
        print("")
    print("=============")  

def returnPlace(board, num):
    for x in reversed(range(6)):
        if board[int(num)][x] == "-":
            return x
    return -1

def checkWin(board):
    check=""
    #VERTICAL WINS
    for x in range(7):
        for y in range(6):
            check+=board[x][y]
        #print(check)
        if ("OOOO" in check or "XXXX" in check):
            return True
        check=""
        
    #HORIZONTAL WINS
    for x in range(6):
        for y in range(7):
            check+=board[y][x]
        #print(check)
        if ("OOOO" in check or "XXXX" in check):
            return True
        check=""

    #DIAGONAL WINS (LEFT TO RIGHT)
    for x in range(7):
        for y in range(6):
            z=0
            while (x+z < 7 and z+y < 6):
                check+=board[x+z][y+z]
                z+=1
            #print(check)
            if ("OOOO" in check or "XXXX" in check):
                return True
            check=""
    #DIAGONAL WINS (RIGHT TO LEFT)
    for x in range(7):
        for y in range(6):
            z=0
            while (x-z < 7 and x-z >=0 and z+y < 6):
                check+=board[x-z][y+z]
                z+=1
            #print(check)
            if ("OOOO" in check or "XXXX" in check):
                return True
            check=""
    return False
    
#GAME
board = createBoard()
print("Welcome to Connect Four!")
while (not win and not tie):
    print("Move: " + str(moves))
    drawBoard(board)
    print("Enter a number 0-6")
    if moves%2 != 0:
        letter = "X"
        player = 1
    else:
        letter = "O"
        player = 2
    num = input("Player " + str(player) + "'s turn: ")
    if num in["0","1","2","3","4","5","6"]:
        place = returnPlace(board,num)
        if place >= 0:
            board[int(num)][place] = str(letter)
            win = checkWin(board)
            if moves == 42 and win == False:
                tie = True
        else:
            print("")
            print("This column is full!")
            print("")
            time.sleep(1)
            continue 
    else:
        print("")
        print("Invalid number!")
        print("")
        time.sleep(1)
        continue
    
    if (win == True or tie == True):
        continue
    print("")
    moves+=1
    
#WIN
print("")
print("Total Moves: " + str(moves))
drawBoard(board)
if win == True:
    print("Player " + str(player) + " wins!")
else:
    print("There was a tie!")
time.sleep(5)

