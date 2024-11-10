# وارد کردن ماژول مورد نیاز
import random

# تابعی که لیستی از ارقام یک عدد را بازمی‌گرداند
def getDigits(num):
    return [int(i) for i in str(num)]  

# تابعی که بررسی می‌کند آیا عدد دارای ارقام تکراری نیست
# اگر تکرار وجود نداشته باشد، True وگرنه False برمی‌گرداند
def noDuplicates(num): 
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False

# تابعی که یک عدد ۴ رقمی با ارقام غیرتکراری تولید می‌کند
def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num

# تابعی که تعداد ارقام مشترک در جای درست (bulls)
# و تعداد ارقام مشترک در جای نادرست (cows) را بازمی‌گرداند
def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)
    
    for i, j in zip(num_li, guess_li):
        
        # بررسی وجود رقم مشترک
        if j in num_li:
            
            # اگر رقم مشترک در جای درست باشد
            if j == i:
                bull_cow[0] += 1
            
            # اگر رقم مشترک در جای نادرست باشد
            else:
                bull_cow[1] += 1
                
    return bull_cow

# تولید کد مخفی
num = generateNum()
tries = int(input('Enter number of tries: ')) # دریافت تعداد تلاش‌ها
count = 0

# اجرای بازی تا زمان درست حدس زدن یا اتمام تعداد تلاش‌ها
while tries > 0:
    guess = int(input("Enter your guess: ")) # دریافت حدس کاربر
    count += 1
    
    # بررسی عدم تکرار ارقام در عدد حدس زده شده
    if not noDuplicates(guess):
        print("Number should not have repeated digits. Try again.")
        continue
    # بررسی اینکه عدد ۴ رقمی باشد
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again.")
        continue
    
    bull_cow = numOfBullsCows(num, guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -= 1
    
    # اگر حدس درست باشد
    if bull_cow[0] == 4:
        print("You guessed right!")
        break
else:
    print(f"You ran out of tries. Number was {num}")

print(f'The number is guessed in {count} tries')
