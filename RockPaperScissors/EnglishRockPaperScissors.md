<div align="center">

# Tic Tac Toe
<img alt="Gif" src="https://i.pinimg.com/originals/3b/f2/f4/3bf2f45865bc4a63a663611ea357de4c.gif" height="250px" width="350px">
</div>
<hr>

[Click to see the descriptions in Persian language](PersianRockPaperScissors.md)
<hr>

[Python Code](RockPaperScissors.py)
## Overview of the Code
This code is a simple implementation of the classic "Rock, Paper, Scissors" game in Python. Here's a breakdown of each part:

1. get_computer_choice Function:
   - This function randomly selects a choice for the computer from the list ["rock", "paper", "scissors"] using Python's random.choice() function. It returns the computer's choice.
2. determine_winner Function:
   - This function takes the user's choice and the computer's choice as input and determines the outcome.
   - It checks if both choices are the same, which would mean a tie.
   - If the choices are different, it determines whether the user wins or the computer wins based on the standard rules of Rock, Paper, Scissors:
       - Rock beats Scissors
       - Scissors beats Paper
       - Paper beats Rock
   - It then returns the result as a string.
3. play_game Function:
   - This function contains the main loop to play the game.
   - It welcomes the player and continually prompts them to enter their choice (or "exit" to end the game).
   - If the user enters "exit," the loop breaks, and the game ends.
   - If the user enters an invalid choice, an error message is shown, and the loop restarts.
   - For valid choices, the computer's choice is displayed, and the outcome of the game is printed based on the result from determine_winner.
4. Game Start:
   - The game is started by calling play_game() at the end of the code, launching the main loop for user interaction.
     
### Key Features
1. <b>Random Computer Choice:</b> Random selection of "rock," "paper," or "scissors" for the computer.
2. <b>Winner Determination:</b> Determines the winner based on game rules, with an option for a tie.
3. <b>User Interaction:</b> Allows multiple rounds and exits with "exit" input.
4. <b>Input Validation:</b> Displays an error message for invalid input.
5. <b>Modular Structure:</b> Readable and editable code with separate functions.

### How the Code Works (Step-by-Step Breakdown):
1. import random:
   - This line imports the random module, which provides tools to generate random numbers or make random selections.
```python
import random
```
2. <b>Functio</b> get_computer_choice:
   - This function randomly selects the computer's choice from the options "rock," "paper," and "scissors." It uses random.choice to select one of the elements in the choices list and returns it as the function's output.
```python
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
```
3. <b>Function</b> determine_winner:
- This function determines the result of the game based on the user's choice and the computer's choice:
   - If both choices are the same, the game is a tie.
   - Conditions for the user to win are checked using elif statements.
   - If none of the winning conditions are met, the computer wins.
```python
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
```
4. <b>Function</b> play_game:
- This function runs the game. Its steps are as follows:
   - Prints a welcome message.
   - Creates a while loop to run the game multiple times until the user enters "exit."
   - If the user's input is "exit," the game ends, and a goodbye message is printed.
   - If the input is invalid, an error message is printed, and the user must choose again.
   - If the input is valid, the computer makes a random choice, and the result of the game is printed using the determine_winner function.
```python
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors, or exit): ")
        if user_choice == "exit":
            print("Game over. Goodbye!")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
```
5. <b>Starting the Game by Calling</b> play_game:
   - Finally, by calling the play_game function, the game starts, and the execution flow enters the previous section.
```python
# Start the game
play_game()
```
This code effectively simulates a simple "Rock, Paper, Scissors" game that can be played by entering inputs in the terminal.

# Python code: 
```python
import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors, or exit): ")
        if user_choice == "exit":
            print("Game over. Goodbye!")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

# Start the game
play_game()
```
