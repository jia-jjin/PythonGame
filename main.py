import number_guessing_game
import word_guessing_game

def welcome():
    print("=========================================")
    print("Welcome to the collection of mini-games!")
    print("protip: This is meant to be a fun side-project, please do not mind the minor bugs and grammatical errors")
    print("=========================================")
    print("Pick a category:")
    print("1. Numbers")
    print("2. Words")
    print("0. More coming soon!")

while True:
    welcome()
    option = int(input())
    if (option == 1):
        number_guessing_game()
    elif (option == 2):
        word_guessing_game()