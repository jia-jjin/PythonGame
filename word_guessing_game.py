from constants import kindergarten_words, letters
import random

def word_guessing_game():
    print("Welcome to the Word Guessing Game!")
    print("I will be choosing a random word for you to guess!")
    print("If the letter you guessed is in the word, all the position of the matching letters will be revealed,")
    print("or else it's a heart wasted!")
    print("==========================================")
    i = random.randint(0, len(kindergarten_words)-1)
    selected_word = kindergarten_words[i]

    letters_left = len(selected_word)
    shown_word = list("_" * letters_left)
    lives = 5

    while (letters_left > 0):
        count = 0
        letter_guessed = input("Start guessing a random letter: ")

        if (letter_guessed not in letters):
            print("Input an alphabet only!")
        else:
            if (letters[letter_guessed] == 1) :
                letters[letter_guessed] = 0
                for j in range(len(selected_word)):
                    if (selected_word[j] == letter_guessed):
                        shown_word[j] = letter_guessed
                        count += 1
                        letters_left -= 1
                if (count == 0):
                    print("Oopsie, it's a miss!")
                    lives -= 1
                else:
                    print("HIT!")
                print("Current word: " + "".join(shown_word))
                print("Current lives: " + "❤️ " * lives + "💔" * (5-lives))
                # print(selected_word)
            else:
                print("Already guessed!")
        print("")

        if (lives == 0):
            print("YOU LOST! PLAY AGAIN TO WIN!💔💔💔")
            print("The word: "+ selected_word)
            return
        
    print("Congrats on beating this game! try again plews?")