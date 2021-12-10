# Author MB 12/09/2021

from random import randint


def rock_paper_scissors():
    """Play rock paper scissors"""
    player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
    computer = randint(0, 2)

    # Check if the user or the computer won.
    if player == computer:
        print("It's a tie!")
        return "tie"
    elif player == 0:
        if computer == 1:
            print("You lose, paper covers rock.\n")
            return "loss"
        else:
            print("You win, rock crushes scissors!\n")
            return "win"
    elif player == 1:
        if computer == 2:
            print("You lose, scissors cuts paper.\n")
            return "loss"
        else:
            print("You win, paper covers rock!\n")
            return "win"
    elif player == 2:
        if computer == 0:
            print("You lose, rock crushes scissors.\n")
            return "loss"
        else:
            print("You win, scissors cuts paper!\n")
            return "win"

win = 0
loss = 0
tie = 0
games = 0

while True:

    play = str.capitalize(input("DO YOU WNAT TO PLAY!? Y or N: "))
    if play == "Y":
        games += 1
        results = rock_paper_scissors()
        if results == "win":
            win += 1
        elif results == "loss":
            loss += 1
        elif results == "tie":
            tie += 1
    elif play == "N":
        print("Out of {3} games played, you have won {0} games, lost {1} games, tied {2} games".format(win, loss, tie, games))
        break
    