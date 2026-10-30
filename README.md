# Python Mini-Game Collection

A small collection of mini-games written in Python! Fun games from the 80's and 90's including Ship Warrior (Plane Shooter), Snake Game, Word Guesser and Number Guesser that can be selected through a simple GUI menu.

## Requirements

- Python 3.10 or later
- Git
- A desktop environment that can opening Tkinter windows.

## Installation

Open terminal and run:

```bash
git clone https://github.com/jia-jjin/PythonGame.git
cd PythonGame
```

## Run the game

From **root folder**, run:

```bash
python main.py
```

or

```bash
python3 main.py
```

## Navigating through

Throughout the program, there will always be selections. For example:

```text
=========================================
Welcome to the collection of mini-games!
=========================================
Pick a game:

1. Number Guessing
2. Word Guessing
3. Snake Game
4. Ship Warrior
0. End conversation
```

Type the number for the game you want and press **Enter**. After the game finishes, the option will pop up and prompt whether you want to continue exploring or end the conversation.

## How to play

### 1. Number Guessing

1. An integer from 1 to 100 is chosen randomly by the computer.
2. Guess the number by typing into the kernel/terminal
3. Only one of these four outputs will be displayed:
    - **Higher!** - The number is higher than your guess.
    - **Lower!** - The number is lower than your guess.
    - **Congrats! You nailed it!** - You nailed it bro
    - **Pick a number from 1 to 100 only!** - you know what that means
4. When the game ends, it will show you the total guesses it took for you to nail the answer. You should get it with less than 10 guesses.

protip: Just use "binary search" technique. [Search it up](https://www.geeksforgeeks.org/dsa/binary-search/) for more information.

### 2. Word Guessing

1. Only letters from the [alphabets list](https://www.worldometers.info/languages/english-alphabet/) are allowed to be guessed.
2. Once you have guessed a letter, the following will be shown:
    - Whether it's a:
        - **HIT!** - the letter is inside the word
        - **Oopsie, it's a miss!** - the letter is NOT inside the word
    - The current word with all letters guessed in the correct positions
    - Current hearts/lives, where each WRONG guess will cost you a heart
    - All letters guessed in alphabetical order
3. If you happen to repeat the same letter in the following guesses, the game is kind enough to remind you and stop you from doing so (without costing any heart).
4. Once you have reached the end of the game, there's only two possible outcomes:
    - You guessed the word. Your remaining hearts will be shown.
    - You couldn't guess the word (me 90% of the time). The game asks you to play again

### 3. Snake Game

The Snake Game opens in a separate window, and the window moves following the snake's movement.

**Controls**

| Key | Description |
|---|---|
| `W` | Move up |
| `A` | Move left |
| `S` | Move down |
| `D` | Move right |
| `Y` | Restart after Game Over |
| `N` | Exit after Game Over |
| `Esc` | Exit |

- Move the snake through the screen to eat fruits (red circle)
- Do not let the snake head touch the white barrier or the own snake body, or else game over!
- The score is shown on the head of the snake.
- Press **Esc** or close the window to exit the game anytime.

### 4. Ship Warrior (Plane Shooter)

## Project structure

```text
PythonGame/
├── main.py
├── constants.py
└── games/
    ├── number_guessing_game.py
    ├── snake_game.py
    ├── word_guessing_game.py
    └── ship_warrior/
        ├── import_turtle.py
        ├── seabackground.gif
        └── ship.py
```

## Notes/Disclaimer

This project aims to serve as a learning platform for both of us. Since this is the first time we are coding in python turtle, we took some inspirations from other projects from the Internet. Although some games are imperfect, they really helped us to master the basics of programming, and soon we believe we will create better projects in the future. Thanks HackClub!
