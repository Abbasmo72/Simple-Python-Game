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

## How the Code Works (Step-by-Step Breakdown)
1. Import Required Libraries:
   - random: Used to generate a random integer for the player to guess.
   - time: Used to add delays, making the game feel more interactive.
```python
import random
import time
```
2. Display Welcome Message:
   - This prints a welcome message and pauses for 3 seconds to give the player time to read it.
```python
print('<<----Welcome to the Guess Number Game---->>')
time.sleep(3)
```
3. Inform the Player About the Range:
   - Informs the player that the number they are trying to guess is between 1 and 100, with a short pause to emphasize the message.
```python
print('<<---between 1 - 100--->>')
time.sleep(2)
```
4. Get Player’s Name:
   - Prompts the player to enter their name and adds a 1-second delay for a smoother user experience.
```python
name = input('What is your name? ')
time.sleep(1)
```
5. Prompt Initial Guess:
   - Takes the player's first guess as an integer input.
```python
guess = int(input('What is your guess?: '))
```
6. Generate the Random Answer:
   - Generates a random number between 1 and 100, which the player will try to guess.
```python
answer = random.randint(1, 100)
```
7. Initialize the Guess Counter:
   - Initializes a counter to keep track of the number of guesses the player makes.
```python
guess_count = 0
```
8. Main Guessing Loop:
   - This loop will continue to run until the player’s guess matches the answer.
   - Each time the loop runs, a 0.5-second delay is added, and the guess_count increments by 1 .
```python
while guess != answer:
    time.sleep(0.5)
    guess_count += 1
```
9. Check Guess Accuracy:
    - If the guess is too high, a message prompts the player to guess a lower number.
    - If the guess is too low, a message prompts the player to guess a higher number.
    - In each case, a new guess is taken and stored in guess.
```python
if guess > answer:
    guess = int(input('Your guess is too high. What is your next guess?: '))
else:
    guess = int(input('Your guess is too low. What is your next guess?: '))
```
10. End Message:
    - Once the player guesses the correct number, a congratulatory message is displayed, showing the player’s name, the correct answer, and the total number of attempts taken.
```python
print(f'Congratulations, {name}! The correct number was {answer}. It took you {guess_count} guesses.')
```

This step-by-step breakdown should make it easy to understand how the code progresses from start to finish.

## Python Code
```python
import random
import time

# Display a welcome message for the game
print('<<----Welcome to the Guess Number Game---->>')
time.sleep(3)

# Inform the player about the range of the number to guess
print('<<---between 1 - 100--->>')
time.sleep(2)

# Prompt the player to enter their name
name = input('What is your name? ')
time.sleep(1)

# Prompt the player to make an initial guess
guess = int(input('What is your guess?: '))

# Randomly select the correct answer between 1 and 100
answer = random.randint(1, 100)

# Initialize the guess count
guess_count = 0

# Loop until the player's guess matches the answer
while guess != answer:
    time.sleep(0.5)
    guess_count += 1
    
    # Provide feedback and prompt for a new guess if the guess is too high
    if guess > answer:
        guess = int(input('Your guess is too high. What is your next guess?: '))
        
    # Provide feedback and prompt for a new guess if the guess is too low
    else:
        guess = int(input('Your guess is too low. What is your next guess?: '))

# Congratulate the player and display the correct answer and the number of guesses taken
print(f'Congratulations, {name}! The correct number was {answer}. It took you {guess_count} guesses.')
```
