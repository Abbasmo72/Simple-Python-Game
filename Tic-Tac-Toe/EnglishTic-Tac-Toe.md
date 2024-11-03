<div align="center">

# Game Cows Bulls
<img alt="Gif" src="https://bartvwezel.nl/wp-content/uploads/2020/09/ezgif.com-video-to-gif-8.gif" height="250px" width="300px">
</div>
<hr>

[Click to see the descriptions in Persian language](PersianTic-Tac-Toe.md)
<hr>

## Overview of the Code
[Python Code](Tic-Tac-Toe/Tic-Tac-Toe.py)
This Python code implements a simple graphical user interface (GUI) for a Tic-Tac-Toe game using the Tkinter library. The game allows a human player to play against an AI opponent. Here's an overview of the code, broken down into key components:

1. Imports:
   - <b>tkinter:</b> Provides tools to create GUI applications.
   - <b>messagebox:</b> Offers dialog boxes for displaying messages to the user.
   - <b>random:</b> Used for randomization (not explicitly needed in this code).

2. Game Logic Functions:
   - <b>check_winner(board, player):</b> This function checks if the specified player (either 'X' or 'O') has won the game by checking all rows, columns, and diagonals.
   - <b>is_board_full(board):</b> Checks if the board is full (no empty spaces) to determine if the game is a draw.
   - <b>minimax(board, depth, is_maximizing):</b> Implements the Minimax algorithm, which is a recursive function that evaluates the board's state to decide the best move for the AI. It returns scores based on winning, losing, or drawing situations.
   - best_move(board): Determines the best move for the AI by evaluating all possible moves using the Minimax algorithm and returning the position of the optimal move.

3. Game Interaction Functions:
   - <b>make_move(row, col):</b> Handles the player's move by updating the board and the GUI. It checks for a win or draw after the player's move and calls the AI's move if the game is still ongoing.
   - <b>ai_move():</b> Executes the AI's move using the best_move() function, updates the board, and checks for a win or draw.

4. GUI Setup:
   - A Tkinter window is created with the title "Tic-Tac-Toe".
   - A 3x3 board is initialized as a list of lists, representing empty spaces.
   - Buttons are created for each cell in the grid, with a command that triggers the make_move function when clicked. Each button updates the GUI to show the current player's symbol ('X' for the human player, 'O' for the AI).

5. Main Loop:
   - The root.mainloop() starts the Tkinter event loop, allowing the GUI to respond to user actions and display updates.

## Key Features
  - The human player plays as 'X' and makes moves by clicking the buttons.
  - The AI plays as 'O' and automatically calculates its moves using the Minimax algorithm.
  - The game ends with a win message for either the player or the AI, or a draw message when the board is full without a winner.
  - Error handling is included to manage invalid moves.

This implementation is a straightforward example of using a GUI to create an interactive game, showcasing both user interaction and basic AI logic.
