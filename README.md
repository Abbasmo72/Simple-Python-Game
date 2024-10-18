## Overview of the Code

[GameBulls&Cows.py](GameBulls&Cows.py)

The provided code implements a text-based version of the "Bulls and Cows" game, a classic guessing game where players try to identify a secret number based on feedback about their guesses. Here's an overview of its key components:

1. Game Objective:
  The goal of the game is for the player to guess a randomly generated four-digit number with unique digits. The player receives feedback in the form of "bulls" and "cows":<br>
    <b>Bulls:</b> Digits that are correct and in the correct position.<br>
    <b>Cows:</b> Digits that are correct but in the wrong position.

2. Key Functions:
  <b>bgetDigits(num)</b>: Converts a number into a list of its individual digits.<br>
  <b>noDuplicates(num):</b> Checks if the given number contains any duplicate digits.<br>
  <b>generateNum()</b>: Generates a random four-digit number without repeated digits.<br>
  <b>numOfBullsCows(num, guess):</b> Compares the secret number with the player's guess and returns the count of bulls and cows.<br>

3. Game Flow:
  The game starts by generating a secret number and asking the player for the number of tries.
  In a loop, the player inputs their guess. The game checks for valid input (no duplicates and four digits).
  After each guess, the player receives feedback on how many bulls and cows they have.  
  The game continues until the player either guesses the correct number or runs out of attempts, at which point the correct number is revealed.

4. Error Handling: The code includes error handling to ensure the player inputs a valid four-digit number without duplicate digits. If the input is invalid, the player is prompted to try again.

5. Outcome:
  At the end of the game, the player is informed if they guessed the number correctly or if they have run out of tries, along with the secret number.

This structured approach to coding allows for easy understanding and extensibility, making it an excellent example of how to implement game logic in Python.
