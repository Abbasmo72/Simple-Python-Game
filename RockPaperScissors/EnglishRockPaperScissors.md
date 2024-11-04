<div align="center">

# Tic Tac Toe
<img alt="Gif" src="https://i.pinimg.com/originals/3b/f2/f4/3bf2f45865bc4a63a663611ea357de4c.gif" height="250px" width="350px">
</div>
<hr>

[Click to see the descriptions in Persian language](PersianRockPaperScissors.md)
<hr>

[Python Code](RockPaperScissors/RockPaperScissors.py)
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
