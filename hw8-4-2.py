# Author MB 12/09/2021

from random import randint

def guessing_game():
    while True:
        player = input ("enter a number 0 & 50: ")
        computer =  randint (0, 50)

        if player != "stop":
            if int(player) == computer:
                print("You guessed the number right, the number was {0} and you guessed {1}".format(computer, player))
                break
            elif int (player) < computer:
                print("You guessed wrong. The answer is higher.")
            elif int (player) > computer:
                print ("You guessed wrong. the number is lower.")
        elif player == "stop":
            print("the number was {0}".format(computer))

guessing_game()