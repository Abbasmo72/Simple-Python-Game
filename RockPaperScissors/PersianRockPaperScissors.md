<div align="center">

# سنگ ،کاغذ ،قیچی
<img alt="Gif" src="https://i.pinimg.com/originals/3b/f2/f4/3bf2f45865bc4a63a663611ea357de4c.gif" height="250px" width="300px">
</div>
<hr>

[Click to see the descriptions in English language](EnglishRockPaperScissors.md)
<hr>

[کد پایتون](RockPaperScissors.py)
## مروری بر کد
این کد یک پیاده سازی ساده از بازی کلاسیک "Rock, Paper, Scissors" در پایتون است. در اینجا به تفکیک هر بخش می پردازیم:
1. تابع get_computer_choice:
- این تابع به صورت تصادفی یکی از گزینه‌های ["rock", "paper", "scissors"] را برای کامپیوتر انتخاب می‌کند و با استفاده از تابع random.choice() در پایتون این کار را انجام می‌دهد. سپس انتخاب کامپیوتر را برمی‌گرداند.
2. این تابع دو ورودی، یکی انتخاب کاربر و دیگری انتخاب کامپیوتر، دریافت می‌کند و نتیجه بازی را تعیین می‌کند.
- این تابع دو ورودی، یکی انتخاب کاربر و دیگری انتخاب کامپیوتر، دریافت می‌کند و نتیجه بازی را تعیین می‌کند.
- ابتدا بررسی می‌کند که آیا انتخاب‌ها یکسان هستند یا خیر، که در این صورت نتیجه "مساوی" خواهد بود.
- اگر انتخاب‌ها متفاوت باشند، بر اساس قوانین بازی سنگ، کاغذ، قیچی تعیین می‌کند که چه کسی برنده است.
3. تابع play_game:
  - این تابع حلقه اصلی برای اجرای بازی را در خود دارد.
  - پیام خوش‌آمدگویی نمایش داده و به طور مداوم از کاربر درخواست می‌کند تا انتخاب خود را وارد کند (یا "exit" برای خروج از بازی).
  - اگر کاربر عبارت "exit" را وارد کند، حلقه شکسته شده و بازی خاتمه می‌یابد.
  - اگر کاربر ورودی نامعتبری وارد کند، پیامی نمایش داده می‌شود و حلقه از نو شروع می‌شود.
  - برای ورودی‌های معتبر، انتخاب کامپیوتر نمایش داده می‌شود و نتیجه بازی بر اساس خروجی تابع determine_winner چاپ می‌شود.
4. شروع بازی:
- با فراخوانی play_game() در انتهای کد، بازی شروع می‌شود و حلقه اصلی برای تعامل با کاربر فعال می‌شود.

این کد تعاملی بوده و به کاربر اجازه می‌دهد تا چندین بار بازی کند تا زمانی که گزینه "exit" را وارد کند. ساختار آن ساده و واضح است و برای افراد مبتدی که در حال یادگیری حلقه‌ها، شرط‌ها و توابع در پایتون هستند، ایده‌آل است.

### ویژگی های کلیدی
1. انتخاب تصادفی کامپیوتر: انتخاب تصادفی "سنگ"، "کاغذ" یا "قیچی" برای کامپیوتر.
2. تعیین برنده: برنده را بر اساس قوانین بازی، با گزینه ای برای تساوی تعیین می کند.
3. تعامل کاربر: چندین دور و خروج با ورودی "خروج" اجازه می دهد.
4. پیام nput Validationb یک پیام خطا برای ورودی نامعتبر نمایش می دهد.
5. ساختار مدولار: کد قابل خواندن و ویرایش با توابع جداگانه.


 ## نحوه کار کد (تجزیه گام به گام):
 1. وترد کردن کتابخانه random:
    - این خط از ماژول random استفاده می‌کند که ابزارهای لازم برای تولید اعداد یا انتخاب‌های تصادفی را فراهم می‌کند.
```python
import random
```
2.  تابع get_computer_choice:
   - این تابع انتخاب کامپیوتر را به صورت تصادفی از بین گزینه‌های "سنگ"، "کاغذ"، و "قیچی" برمی‌گرداند. با استفاده از random.choice، یکی از عناصر لیست choices انتخاب و به عنوان خروجی این تابع برگردانده می‌شود.
```python
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
```
3. تابع determine_winner:
- این تابع نتیجه بازی را بر اساس انتخاب‌های بازیکن و کامپیوتر تعیین می‌کند:
   - اگر هر دو انتخاب مشابه باشند، بازی مساوی است.
   - اگر هر دو انتخاب مشابه باشند، بازی مساوی است.
   - در غیر این صورت، کامپیوتر برنده می‌شود.

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
4. تابع play_game:
- این تابع بازی را اجرا می‌کند. مراحل آن به شرح زیر است:
   - چاپ پیام خوش‌آمدگویی.
   - ایجاد یک حلقه while برای اجرای چندباره بازی تا زمانی که کاربر "exit" را وارد کند.
   - اگر ورودی کاربر "exit" باشد، بازی خاتمه می‌یابد و پیام خداحافظی چاپ می‌شود.
   - اگر ورودی معتبر نباشد، پیام خطا چاپ و کاربر باید دوباره انتخاب کند.
   - اگر ورودی معتبر باشد، کامپیوتر یک انتخاب تصادفی می‌کند و نتیجه بازی با استفاده از تابع determine_winner چاپ می‌شود.
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
5. شروع بازی با فراخوانی play_game:
   - در نهایت، با فراخوانی تابع play_game، بازی آغاز می‌شود و اجرای آن از بخش قبلی به جریان می‌افتد.

```python
# Start the game
play_game()
```
این کد به‌طور کامل یک بازی ساده "سنگ، کاغذ، قیچی" را شبیه‌سازی می‌کند که می‌توان آن را با وارد کردن ورودی‌ها در ترمینال انجام داد.

# کد پایتون:
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
 
