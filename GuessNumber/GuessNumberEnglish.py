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
