# import sys
# import random
# from enum import Enum

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSOR = 3

# playagain = True
# while playagain:

#     playerchoice = input('Enter...\n1 for rock\n2 for paper\n3 for scissor\n\n')

#     try:
#         player = int(playerchoice)
#     except ValueError:
#         print('\nhey this isnt even a number dude\n')
#         continue

#     if player < 1 or player > 3:
#         print('\nyou must pick a number 1-3\n')
#         continue

#     computerchoice = random.choice('123')
#     computer = int(computerchoice)

#     print('\nyou choose ' + str(RPS(player)).replace('RPS.','') + '.')
#     print('Python choose ' + str(RPS(computer)).replace('RPS.', '') + '.\n')

#     if player == 1 and computer == 3:
#         print('you win!')
#     elif player == 2 and computer == 1:
#         print('you win!')
#     elif player == 3 and computer == 2:
#         print('you win!')
#     elif player == computer:
#         print('draw')
#     else:
#         print("python wins")

#     while True:
#             playagain = input('\nPlay Again?\nY for Yes\nor Q to Quit\n\n').lower()

#             if playagain == 'y':
#                 break
#             elif playagain == 'q':
#                 print('\nSee you later!')
#                 print('Come back again!\n')
#                 sys.exit(0)
#             else:
#                 print('You didn\'t pick Y or Q, let\'s try again\n')

#             if playagain == 'q':
#              break
# --------------.
# import sys
# import random
# from enum import Enum

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSOR = 3

# print(' ')
# print('Enter...\n1 for rock\n2 for paper\n3 for scissor\n')
# playerchoice = input()

# try:
#     player = int(playerchoice)
#     if player < 1 or player > 3:
#         sys.exit('You must pick a number 1-3')
# except ValueError:
#     sys.exit('Hey, this isnt even a number, dude')

# computer = random.choice(list(RPS))

# print('')
# print('You choose ' + str(RPS(player)) + '.')
# print('Python chooses ' + str(computer) + '.')
# print('')

# if player == RPS.ROCK.value and computer == RPS.SCISSOR:
#     print('You win!')
# elif player == RPS.PAPER.value and computer == RPS.ROCK:
#     print('You win!')
# elif player == RPS.SCISSOR.value and computer == RPS.PAPER:
#     print('You win!')
# elif player == computer.value:
#     print('Draw')
# else:
#     print('Python wins')

# -------------------------
# import sys
# import random

# choices = ["rock", "paper", "scissors"]

# print(' ')
# print('Enter...\n1 for rock\n2 for paper\n3 for scissors\n')
# playerchoice = input()

# try:
#     player = int(playerchoice)
#     if player < 1 or player > 3:
#         sys.exit('You must pick a number 1-3')
# except ValueError:
#     sys.exit('Hey, this isnt even a number, dude')

# computer_choice = random.choice(choices)

# print('')
# print('You choose ' + choices[player - 1] + '.')
# print('Python chooses ' + computer_choice + '.')
# print('')

# if player == 1 and computer_choice == "scissors":
#     print('You win!')
# elif player == 2 and computer_choice == "rock":
#     print('You win!')
# elif player == 3 and computer_choice == "paper":
#     print('You win!')
# elif player == choices.index(computer_choice) + 1:
#     print('Draw')
# else:
#     print('Python wins')
# ---------------
# import sys
# import random
# from enum import Enum

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSOR = 3

# def play_rps():
#     while True:
#         print(' ')
#         playerchoice = input('Enter...\n1 for rock\n2 for paper\n3 for scissor\n\n')

#         try:
#             player = int(playerchoice)
#         except ValueError:
#             print('Hey, this isn\'t even a number!')
#             continue

#         if player < 1 or player > 3:
#             print('You must pick a number 1-3')
#             continue

#         computer = random.randint(1, 3)

#         print('')
#         print('You choose ' + str(RPS(player)).split('.')[1] + '.')
#         print('Python chooses ' + str(RPS(computer)).split('.')[1] + '.')
#         print('')

#         while True:
#             playagain = input('\nPlay Again?\nY for Yes\nor Q to Quit\n\n').lower()

#             if playagain == 'y':
#                 break
#             elif playagain == 'q':
#                 print('\nSee you later!')
#                 print('Come back again!\n')
#                 sys.exit(0)
#             else:
#                 print('You didn\'t pick Y or Q, let\'s try again\n')

#         if playagain == 'q':
#             break

# if __name__ == "__main__":
#     play_rps()
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


playagain = True
while playagain:
    print(' ')
    playerchoice = input(
        'Enter...\n1 for rock\n2 for paper\n3 for scissor\n\n')

    try:
        player = int(playerchoice)
    except ValueError:
        sys.exit('Hey, this isn\'t even a number, dude')

    if player < 1 or player > 3:
        sys.exit('You must pick a number 1-3')

    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print('')
    print('You choose ' + str(RPS(player)).replace('RPS.', '') + '.')
    print('Python choose ' + str(RPS(computer)).replace('RPS.', '') + '.')
    print('')

    if player == 1 and computer == 3:
        print('You win!')
    elif player == 2 and computer == 1:
        print('You win!')
    elif player == 3 and computer == 2:
        print('You win!')
    elif player == computer:
        print('Draw')
    else:
        print("Python wins")

    while True:
        playagain = input('\nPlay Again?\nY for Yes\nor Q to Quit\n\n').lower()

        if playagain == 'y':
            break
        elif playagain == 'q':
            print('\nSee you later!')
            print('Come back again!\n')
            sys.exit(0)
        else:
            print('You didn\'t pick Y or Q, let\'s try again\n')

    if playagain == 'q':
        print('Byebye!')
        sys.exit(0)
