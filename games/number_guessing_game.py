import random

def number_guessing_game():
    print("--------- NUMBER GUESSING GAME ---------")
    print("Welcome to the number guessing game!")
    print("I will be picking a random number between 1 and 100 (inclusive).")
    print("Type in a random number and I will tell whether it's higher or lower!")

    target = random.randint(1,100)
    guess = 0
    total_guesses = 0

    while (guess != target):
        guess = int(input("Enter a number: "))
        if (guess > target):
            print("Lower!")
        elif (guess < target):
            print("Higher!")
        total_guesses += 1

    print("Congrats! You nailed it!")
    print("Here\'s some candy 🍭🍬")
    print("Total guesses: " + str(total_guesses))