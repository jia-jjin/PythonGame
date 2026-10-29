from games.number_guessing_game import number_guessing_game
from games.word_guessing_game import word_guessing_game
import time

def welcome():
    print("=========================================")
    print("Welcome to the collection of mini-games!")
    print("protip: This is meant to be a fun side-project, please do not mind the minor bugs and grammatical errors")
    print("=========================================")
    print("Pick a category:")
    print("1. Numbers")
    print("2. Words")
    print("0. End conversation")

def game_end():
    print("=========================================")
    print("I bet you had a lot of fun!")
    print("One more?")
    print("Pick an option:")
    print("1. Go to game menu")
    print("0. End conversation")

while True:
    welcome()

    # check for user input
    option = int(input())
    match option:
        case 1:
            number_guessing_game()
        case 2:
            word_guessing_game()
        case 0:
            print("Thank you for playing!")
            break
        case _:
            print("No such option")
            time.sleep(1.5)
            continue

    # add slight delay for users to see the output
    time.sleep(1.5)

    # display end message, provide option for player to try other games
    game_end()

    # check for user input
    option = int(input())
    match option:
        case 1:
            continue
        case 0:
            print("See you soon!")
            break
        case _:
            print("No such option")
            time.sleep(1.5)
            continue