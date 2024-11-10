<div align="center">

# Guess Number
<img src="https://media2.giphy.com/media/kuofpmsWLJxTk2oDaS/200w.gif?cid=6c09b9522jzqy0ngpj5tjq31iilcgr834755ckwurnwn2jcw&ep=v1_gifs_search&rid=200w.gif&ct=g" alt="Image Description" width="30%">
</div>
<hr>

[Click to see the descriptions in Persian language](GuessNumberPersian.md)
<hr>

[Python Code](GuessNumberEnglish.py)

## Overview of the Code
This code is a simple guessing game in Python where the player tries to guess a randomly generated number between 1 and 100. Here's an overview of each part:
1. <b>Introduction and Instructions:</b> The game starts by displaying a welcome message and then informs the player that the target number will be between 1 and 100.
2. <b>User Setup:</b> The player is asked to enter their name, and then their initial guess is taken.
3. <b>Generate the Answer:</b> A random number is selected as the answer using random.randint(1, 100).
4. <b>Initialize Guess Counter:</b> The game keeps track of how many guesses the player makes, starting with guess_count = 0.
5. <b>Guessing Loop:</b> A loop continues until the player’s guess matches the answer. After each incorrect guess:
   - The code checks if the guess is too high or too low and provides feedback.
   - The player is prompted for a new guess based on this feedback.
6. <b>Success Message:</b> When the correct guess is made, the game congratulates the player, displaying the answer and the total number of guesses they took to find it.

This code is a basic yet engaging number guessing game that provides real-time feedback and counts attempts, offering a straightforward introduction to loops, conditionals, and user input in Python.
