Tic Tac Toe Game

A Python-based command-line implementation of the classic Tic Tac Toe game, developed for the CodeUtsava Hackathon.
This project demonstrates the use of basic control structures, user interaction, and logical flow in Python through a simple but complete game.

Features

Single-player mode (player vs. computer)

Player can choose to play as X or O

Automatic win and draw detection after every move

Clear and minimal text-based interface

No external libraries required — runs on standard Python

How It Works

The game board is represented by a one-dimensional Python list of nine elements, each corresponding to a position on a 3×3 grid.
At the start, all elements are initialized to 0, representing empty cells. The player and computer use 1 and 2 respectively to mark their moves.

Core Logic Breakdown

Player Setup
The player chooses their symbol (X or O) at the beginning. Based on this, numeric representations (1 or 2) are assigned for internal logic.

Move Input and Validation
The player is prompted to select a grid position using numbers 0–8.
The code checks if the position is available in the list of open spots before accepting the move. If not, the player is asked to try again.

Computer Move Generation
The computer selects a random available position from the remaining open spots using Python’s random.choice() function.
This ensures fairness while keeping the logic simple and easy to follow.

Win Condition Checking
After every move, the program checks all eight possible winning combinations (three rows, three columns, and two diagonals).
If any of these combinations are fully occupied by one player’s symbols, that player is declared the winner immediately.

Draw Detection
If all positions are filled and no winner is found, the game declares a draw.

Display
After each round, the current state of the board is displayed using X, O, and - for empty spaces.
This allows the player to visualize the game progress clearly in the console.
