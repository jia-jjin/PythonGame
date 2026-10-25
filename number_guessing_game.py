import random

def number_guessing_game():
    print("Welcome to the number guessing game!")
    print("I will be picking a random number between 1 and 100 (inclusive).")
    print("Type in a random number and I will tell whether it's higher or lower!")

    target = random.randint(1,100)
    guess = 0

    while (guess != target):
        guess = int(input("Enter a number: "))
        if (guess > target):
            print("Lower!")
        elif (guess < target):
            print("Higher!")

    print("Congrats! You nailed it!")
    print("Here\'s some candy 🍭🍬")