<div align="center">

# Tic Tac Toe
<img alt="Gif" src="https://bartvwezel.nl/wp-content/uploads/2020/09/ezgif.com-video-to-gif-8.gif" height="250px" width="300px">
</div>
<hr>

[Click to see the descriptions in Persian language](PersianTic-Tac-Toe.md)
<hr>

## Overview of the Code
[Python Code](Tic-Tac-Toe/Tic-Tac-ToeEnglish.py)

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

### Key Features
  - The human player plays as 'X' and makes moves by clicking the buttons.
  - The AI plays as 'O' and automatically calculates its moves using the Minimax algorithm.
  - The game ends with a win message for either the player or the AI, or a draw message when the board is full without a winner.
  - Error handling is included to manage invalid moves.

This implementation is a straightforward example of using a GUI to create an interactive game, showcasing both user interaction and basic AI logic.

## How the Code Works (Step-by-Step Breakdown):

1. Importing Libraries
```python
import tkinter as tk #provides a library of basic elements of GUI widgets
from tkinter import messagebox #provides a different set of dialogues that are used to display message boxes
import random
```
   - <b>tkinter:</b> This library is used to create a graphical user interface (GUI) and its various elements.
   - <b>messagebox:</b> This module helps to display dialogues for showing messages to the user (such as win or error messages).
   - <b>random:</b> This module is used for randomization, although it is not utilized in the current code.

2. Defining the check_winner Function
```python
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
```
   - This function checks whether the specified player (player, which can be 'X' or 'O') has won the game.
   - It uses two loops to check all rows and columns.
   - It also checks the two diagonals of the board.
   - If a winner is found, it returns True; otherwise, it returns False.

3. Defining the is_board_full Function
```python
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)
```
   - This function checks whether the board is full (meaning there are no empty spaces).
   - It uses nested lists to check all cells.
   - If all cells are filled, it returns True; otherwise, it returns False.

4. Defining the minimax Function
```python
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if is_board_full(board): #if game is full, terminate
        return 0

    if is_maximizing: #recursive approach that fills board with Os
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False) #recursion
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else: #recursive approach that fills board with Xs
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True) #recursion
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval
```
   - This function implements the Minimax algorithm used to compute the best move.
   - It first checks if there is a winner and returns the corresponding score (-1 for 'X' and 1 for 'O').
   - If the board is full, it returns a score of 0.
   - If it is AI's turn (is_maximizing), it evaluates all possible moves to find the best score.
   - If it is the human player's turn, it calculates the score for moves to minimize the score.

5. Defining the best_move Function
```python
def best_move(board):
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move
```
   - This function finds the best move for the AI.
   - It evaluates all possible moves (empty cells) to determine the best score using minimax.
   - It returns the best move (as a tuple of row and column).

6. Defining the make_move Function
```python
def make_move(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        buttons[row][col].config(text='X')
        if check_winner(board, 'X'):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            root.quit()
        elif is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            root.quit()
        else:
            ai_move()
    else:
        messagebox.showerror("Error", "Invalid move")
```
   - This function manages the player's move.
   - It first checks if the cell is empty.
   - If it is empty, it places 'X' in that cell and updates the display.
   - It then checks if the player has won or if the board is full, displaying appropriate messages if needed.
   - If the game continues, it calls the AI's move.
   - If the cell is not empty, it shows an error message.

7. Defining the ai_move Function
```python
def ai_move():
    row, col = best_move(board)
    board[row][col] = 'O'
    buttons[row][col].config(text='O')
    if check_winner(board, 'O'):
        messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
        root.quit()
    elif is_board_full(board):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        root.quit()
```
   - This function executes the AI's turn.
   - It calculates the best move using best_move and places 'O' in the board.
   - It checks if the AI has won or if the board is full, displaying the appropriate messages.

8. Creating and Running the GUI
```python
root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = []

for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text=' ', font=('normal', 30), width=5, height=2, command=lambda row=i, col=j: make_move(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

root.mainloop()
```
   - The main Tkinter window is created, and the title "Tic-Tac-Toe" is set.
   - A 3x3 board is created to represent the game state.
   - Buttons for each cell in the board are created, and clicking on them triggers the make_move function.
   - root.mainloop() starts the main event loop, allowing the program to respond to user interactions.

This code fully implements a Tic-Tac-Toe game with game logic and a graphical user interface, allowing a human player to compete against an AI.

# Python Code
```python
import tkinter as tk #provides a library of basic elements of GUI widgets
from tkinter import messagebox #provides a different set of dialogues that are used to display message boxes
import random

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if is_board_full(board): #if game is full, terminate
        return 0

    if is_maximizing: #recursive approach that fills board with Os
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False) #recursion
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else: #recursive approach that fills board with Xs
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True) #recursion
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

#determines the best move for the current player and returns a tuple representing the position
def best_move(board):
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

def make_move(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        buttons[row][col].config(text='X')
        if check_winner(board, 'X'):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            root.quit()
        elif is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            root.quit()
        else:
            ai_move()
    else:
        messagebox.showerror("Error", "Invalid move")

#AI's turn to play
def ai_move():
    row, col = best_move(board)
    board[row][col] = 'O'
    buttons[row][col].config(text='O')
    if check_winner(board, 'O'):
        messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
        root.quit()
    elif is_board_full(board):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        root.quit()

root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = []

for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text=' ', font=('normal', 30), width=5, height=2, command=lambda row=i, col=j: make_move(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

root.mainloop()
```
