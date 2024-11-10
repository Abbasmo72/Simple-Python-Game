import random

# Function to randomly choose the computer's choice (rock, paper, or scissors)
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner based on user and computer choices
def determine_winner(user_choice, computer_choice):
    # If the user and computer choices are the same, it's a tie
    if user_choice == computer_choice:
        return "It's a tie!"
    # Conditions where the user wins
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    # Otherwise, the computer wins
    else:
        return "Computer wins!"

# Main game function that handles user input and runs the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        # Prompt user for their choice
        user_choice = input("Enter your choice (rock, paper, scissors, or exit): ")
        
        # If the user enters 'exit', end the game
        if user_choice == "exit":
            print("Game over. Goodbye!")
            break
        # Check if user input is valid
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue

        # Get computer's choice
        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice}")
        
        # Determine and display the game result
        result = determine_winner(user_choice, computer_choice)
        print(result)

# Start the game
play_game()
