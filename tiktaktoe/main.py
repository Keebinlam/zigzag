import random
board = ["_", "_", "_",
         "_",  "_",  "_",
         "_",  "_",  "_",]
currentplayer = "X"
winner = None
gamerunning = True

# the board


def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("_________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("_________")
    print(board[6] + " | " + board[7] + " | " + board[8])

# taking player input


def playerinput(board):
    while True:
        inp = int(input("Please enter a number from 1 - 9:"))
        if inp >= 1 and inp <= 9:
            if board[inp - 1] == "_":
                board[inp - 1] = currentplayer
                break
            else:
                print("That spot is already taken. Try again.")
        else:
            print("Invalid input. Please enter a number from 1 - 9.")

# the computer's input


def computerinput(board):
    while currentplayer == "O":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            switchplayer()

# the ways to win


def winrow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True


def wincolm(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True


def windag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True

# checking for winner


def checkwin():
    global gamerunning
    if wincolm(board) or windag(board) or winrow(board):
        print(f"The winner is {winner}")
        gamerunning = False
# check for tie in game


def checktie(board):
    global gamerunning
    if "_" not in board:
        printboard(board)
        print("Tie game!")
        gamerunning = False

# switching players


def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"


while gamerunning:
    print('________________________________')
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    printboard(board)
    switchplayer()
    computerinput(board)
    checktie(board)
    checkwin()
    print('________________________________')
