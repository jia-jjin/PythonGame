from games.number_guessing_game import number_guessing_game
from games.word_guessing_game import word_guessing_game
from games.snake_game import snake_game
from games.ship_warrior.ship import ship_warrior
import time

def convert_to_int(option):
    try:
        return int(option)
    except ValueError:
        return "not selected"

def welcome():
    print("=========================================")
    print("Welcome to the collection of mini-games!")
    print("protip: This is meant to be a fun side-project, please do not mind the minor bugs and grammatical errors")
    print("=========================================")
    print("Pick a game:")
    print("1. Number Guessing")
    print("2. Word Guessing")
    print("3. Snake Game")
    print("4. Ship Warrior")
    print("5. How to play?")
    print("0. End conversation")

def how_to_play():
    print("=========================================")
    print("Select a game to learn how to play:")
    print("1. Number Guessing")
    print("2. Word Guessing")
    print("3. Snake Game")
    print("4. Ship Warrior")
    print("0. Go to game menu")
    # check for user input
    option = convert_to_int(input("Enter a number and press ENTER: "))
    match option:
        case 1:
            print("=========================================")
            print(
"""How to play Number Guessing Game?

1. An integer from 1 to 100 is chosen randomly by the computer.
2. Guess the number by typing into the kernel/terminal
3. Only one of these four outputs will be displayed:
    - Higher! - The number is higher than your guess.
    - Lower! - The number is lower than your guess.
    - Congrats! You nailed it! - You nailed it bro
    - Pick a number from 1 to 100 only! - you know what that means
4. When the game ends, it will show you the total guesses it took for you to nail the answer. You should get it with less than 10 guesses.

protip: Just use "binary search" technique.
""")
        case 2:
            print("=========================================")
            print(
"""How to play Word Guessing Game?

1. Only letters from the alphabets list are allowed to be guessed.
2. Once you have guessed a letter, the following will be shown:
    - Whether it's a:
        - HIT! - the letter is inside the word
        - Oopsie, it's a miss! - the letter is NOT inside the word
    - The current word with all letters guessed in the correct positions
    - Current hearts/lives, where each WRONG guess will cost you a heart
    - All letters guessed in alphabetical order
3. If you happen to repeat the same letter in the following guesses, the game is kind enough to remind you and stop you from doing so (without costing any heart).
4. Once you have reached the end of the game, there's only two possible outcomes:
    - You guessed the word. Your remaining hearts will be shown.
    - You couldn't guess the word (me 90\% of the time). The game asks you to play again
""")
        case 3:
            print("=========================================")
            print(
"""How to play Snake Game?

Snake Game opens in a separate window, and the window moves following the snake's movement.

Controls

W: Move up
A: Move left
S: Move down
D: Move right
Y: Restart after Game Over
N: Exit after Game Over
Esc: Exit

- Move the snake through the screen to eat fruits (red circle)
- Do not let the snake head touch the white barrier or the own snake body, or else game over!
- The score is shown on the head of the snake.
- Press Esc or close the window to exit the game anytime.
""")
        case 4:
            print("=========================================")
            print(
"""How to play Ship Warrior?

Ship Warrior opens in a separate window.

Controls

Space: Fire bullets
W: Accelerate forward
A: Rotate anticlockwise / left
S: Brake
D: Rotate clockwise / right
E: Start the game
Esc: Exit

- On the start screen, press E to proceed with the game.
- Move the ship through the map using WASD. Touching the barrier bounces you off.
- There are three and only three types of entities in this game:
    - Black triangle - Player. This is You.
    - Squares - Enemies. They shoot bullets, so make sure you get around their attacks to shoot at them. Here are the different types:
        - Red: Comes for you aggressively to shoot at you.
        - Yellow: Stays put and does not move. Serves as a landmine, so watch where you're going!
        - Purple: They are the surveillance that goes as far away as possible from you to stay alive.
    - Blue circle - Teammates. They are on the same team as you, which deals damage to the enemies. Shooting at them deducts your scores!
- The score, lives remaining and current level is shown on the head of the snake.
- Press Esc or close the window to exit the game anytime.

tips to earn a high score: kill enemies and protect teammates!
""")
        case 0:
            return
        case _:
            print("No such option")
            time.sleep(1.5)
            return
    input("Press Enter to continue...")

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
    option = convert_to_int(input("Enter a number and press ENTER: "))
    match option:
        case 1:
            number_guessing_game()
        case 2:
            word_guessing_game()
        case 3:
            snake_game()
        case 4:
            ship_warrior()
        case 5:
            how_to_play()
            continue
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
    option = convert_to_int(input("Enter a number and press ENTER: "))
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