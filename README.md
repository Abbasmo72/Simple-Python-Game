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

## How the Code Works (Step-by-Step Breakdown):

The provided code implements a "Bulls and Cows" game where a player tries to guess a randomly generated four-digit number without repeating digits. Here’s a detailed analysis of how the code functions step by step:

1. Import Required Module
```python
import random
```
The code begins by importing the random module, which is used to generate random numbers.

2. Function to Get Digits
   The code contains several functions that serve distinct purposes:<br>
  a. getDigits(num)
 ```python
def getDigits(num): 
    return [int(i) for i in str(num)]
```
Purpose: This function takes an integer num and converts it into a list of its individual digits.
Functionality: The number is first converted to a string, allowing iteration over each character. Each character is then converted back to an integer and returned as a list. For example, if num is 1234, the function returns [1, 2, 3, 4].

  b. noDuplicates(num)
```python
def noDuplicates(num): 
    num_li = getDigits(num) 
    if len(num_li) == len(set(num_li)): 
        return True
    else: 
        return False
```
Purpose: This function checks whether a given number contains any duplicate digits.
Functionality: It converts the number to a list of digits using getDigits(num) and then compares the length of this list to the length of the set created from it. Since sets cannot contain duplicates, a mismatch indicates duplicates exist. The function returns True if no duplicates are found, otherwise False.
  
c. generateNum()
```python
def generateNum(): 
    while True: 
        num = random.randint(1000,9999) 
        if noDuplicates(num): 
            return num 
```
Purpose: This function generates a random four-digit number that has no repeated digits.
Functionality: It repeatedly generates a random integer between 1000 and 9999. For each generated number, it checks for duplicates using noDuplicates(num). Once a valid number is found, it returns that number.

  d. numOfBullsCows(num, guess)
  ```python
def numOfBullsCows(num, guess): 
    bull_cow = [0, 0] 
    num_li = getDigits(num) 
    guess_li = getDigits(guess) 

    for i, j in zip(num_li, guess_li): 
        if j in num_li: 
            if j == i: 
                bull_cow[0] += 1
            else: 
                bull_cow[1] += 1

    return bull_cow 
```
<b>Purpose:</b> This function calculates the number of bulls and cows between the secret number (num) and the player's guess (guess).

<b>Functionality:</b>
It initializes a list bull_cow to keep track of bulls (correct digit in the correct position) and cows (correct digit in the wrong position).
The digits of both the secret number and the guess are extracted using getDigits().
The function then iterates through the digits of both lists. For each digit, it checks if the digit in the guess is present in the secret number.
If a digit matches in both value and position, it is counted as a bull; if it matches in value only, it is counted as a cow.
Finally, the function returns the counts of bulls and cows.

3. Game Initialization
```python
num = generateNum() 
tries = int(input('Enter number of tries: ')) 
count = 0
```
<b>Purpose:</b> The game begins by generating a secret number using generateNum(). The player is prompted to enter the number of attempts they wish to have to guess the number, and a counter (count) is initialized to keep track of the number of guesses made.

4. Game Loop
```python
while tries > 0: 
    guess = int(input("Enter your guess: ")) 
    count += 1
    
    if not noDuplicates(guess): 
        print("Number should not have repeated digits. Try again.") 
        continue
    if guess < 1000 or guess > 9999: 
        print("Enter 4 digit number only. Try again.") 
        continue
    
    bull_cow = numOfBullsCows(num, guess) 
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows") 
    tries -= 1
    
    if bull_cow[0] == 4: 
        print("You guessed right!") 
        break
else: 
    print(f"You ran out of tries. Number was {num}")

print(f'The number is a guess {count}') 
```

5. Conclusion:
   
    This implementation of the Bulls and Cows game showcases several important programming concepts, such as:<br>
	Functions: Encapsulating behavior into reusable blocks.<br>
	Loops: Using loops to allow for repeated interaction until a condition is met.<br>
	Conditionals: Implementing conditional logic to guide the flow of the program based on user input and game rules.

## Potential Improvements

User Interface: The game could be improved with a graphical user interface (GUI) to enhance user experience.<br>
Scoring System: Implementing a scoring system based on the number of tries could add an additional layer of competition.<br>
Multiple Difficulty Levels: Introducing varying lengths of numbers (e.g., 3, 4, or 5 digits) could cater to players of different skill levels.<br>
Game History: Keeping track of previous guesses and providing feedback could further assist players in strategizing their guesses.<br>

## Libraries Used
random: For generating random numbers.<br>
json: While the json library is imported, it is not utilized in this code. It could be useful if you plan to extend the game to save or load game states.<br>

This detailed analysis can be used for documentation or uploading to GitHub, helping users understand the code's structure, functionality, and potential enhancements.

## Python Code
```python
# Import required module 
import random 

# Returns list of digits 
# of a number 
def getDigits(num): 
	return [int(i) for i in str(num)]  
	
	

# Returns True if number has 
# no duplicate digits 
# otherwise False	 
def noDuplicates(num): 
	num_li = getDigits(num) 
	if len(num_li) == len(set(num_li)): 
		return True
	else: 
		return False


# Generates a 4 digit number 
# with no repeated digits	 
def generateNum(): 
	while True: 
		num = random.randint(1000,9999) 
		if noDuplicates(num): 
			return num 


# Returns common digits with exact 
# matches (bulls) and the common 
# digits in wrong position (cows) 
def numOfBullsCows(num,guess): 
	bull_cow = [0,0] 
	num_li = getDigits(num) 
	guess_li = getDigits(guess) 
	
	for i,j in zip(num_li,guess_li): 
		
		# common digit present 
		if j in num_li: 
		
			# common digit exact match 
			if j == i: 
				bull_cow[0] += 1
			
			# common digit match but in wrong position 
			else: 
				bull_cow[1] += 1
				
	return bull_cow 
	
	
# Secret Code 
num = generateNum() 
tries =int(input('Enter number of tries: ')) 
count = 0
# Play game until correct guess 
# or till no tries left 
while tries > 0: 
	guess = int(input("Enter your guess: ")) 
	count += 1
	
	if not noDuplicates(guess): 
		print("Number should not have repeated digits. Try again.") 
		continue
	if guess < 1000 or guess > 9999: 
		print("Enter 4 digit number only. Try again.") 
		continue
	
	bull_cow = numOfBullsCows(num,guess) 
	print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows") 
	tries -=1
	
	if bull_cow[0] == 4: 
		print("You guessed right!") 
		break
else: 
	print(f"You ran out of tries. Number was {num}")

print(f'The number is a guess{count}')	

```













