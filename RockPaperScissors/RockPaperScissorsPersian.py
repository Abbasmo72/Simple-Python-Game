import random

# تابعی برای انتخاب تصادفی گزینه کامپیوتر (سنگ، کاغذ، یا قیچی)
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# تابعی برای تعیین برنده بازی با توجه به انتخاب کاربر و انتخاب کامپیوتر
def determine_winner(user_choice, computer_choice):
    # اگر انتخاب کاربر و کامپیوتر یکسان باشد، بازی مساوی است
    if user_choice == computer_choice:
        return "It's a tie!"
    # شرایطی که کاربر برنده می‌شود
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    # در غیر این صورت، کامپیوتر برنده است
    else:
        return "Computer wins!"

# تابع اصلی بازی که شامل دریافت انتخاب کاربر و اجرای بازی است
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        # درخواست انتخاب کاربر
        user_choice = input("Enter your choice (rock, paper, scissors, or exit): ")
        
        # اگر کاربر گزینه خروج را وارد کند، بازی متوقف می‌شود
        if user_choice == "exit":
            print("Game over. Goodbye!")
            break
        # بررسی اعتبار ورودی کاربر
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue

        # دریافت انتخاب کامپیوتر
        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice}")
        
        # تعیین و نمایش نتیجه بازی
        result = determine_winner(user_choice, computer_choice)
        print(result)

# شروع بازی
play_game()
