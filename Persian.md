<div align="center">

# بازی گاو نر
<img src="https://i.pinimg.com/originals/5a/77/67/5a7767d8ce416e8bae383448cdcfadc4.gif" height="250px" width="500px">
</div>
<hr>

[Click to see the descriptions in English language](Persian.md)
<hr>

## بررسی اجمالی کد
[بازی گاو نر](GameBulls&Cows.py)
کد ارائه شده یک نسخه متنی از بازی "بولز و گاو" را پیاده سازی می کند، یک بازی حدس زدن کلاسیک که در آن بازیکنان سعی می کنند یک عدد مخفی را بر اساس بازخورد در مورد حدس های خود شناسایی کنند. در اینجا مروری بر اجزای اصلی آن است:
1. هدف بازی:
هدف بازی این است که بازیکن یک عدد چهار رقمی به طور تصادفی با ارقام منحصر به فرد را حدس بزند. بازیکن بازخوردی را به شکل "گاو" و "گاو" دریافت می کند:<br>
    - <b>Bulls:</b> ارقامی که صحیح و در موقعیت صحیح هستند.<br>
    - <b>گاو:</b> ارقامی که صحیح هستند اما در موقعیت اشتباه قرار دارند.
2. توابع کلیدی:
- <b>bgetDigits(num)</b>: یک عدد را به لیستی از ارقام جداگانه آن تبدیل می کند.<br>
  - <b>noDuplicates(num):</b> بررسی می کند که آیا شماره داده شده دارای ارقام تکراری است یا خیر.<br>
  - <b>generateNum()</b>: یک عدد چهار رقمی تصادفی بدون ارقام تکراری ایجاد می کند.<br>
  - <b>numOfBullsCows(num, guess):</b> عدد مخفی را با حدس بازیکن مقایسه می کند و تعداد گاوها و گاوها را برمی گرداند.<br>
3. جریان بازی:
 - بازی با ایجاد یک شماره مخفی و درخواست از بازیکن برای تعداد تلاش شروع می شود.
  - در یک حلقه، بازیکن حدس خود را وارد می کند. بازی ورودی معتبر را بررسی می کند (بدون تکرار و چهار رقم).
  - پس از هر حدس، بازیکن در مورد تعداد گاو نر و گاو بازخورد دریافت می کند.  
  - بازی تا زمانی ادامه می یابد که بازیکن یا تعداد صحیح را حدس بزند یا تلاش هایش تمام شود، در این مرحله تعداد صحیح مشخص می شود.
4. مدیریت خطا: کد شامل رسیدگی به خطا می شود تا اطمینان حاصل شود که بازیکن یک عدد چهار رقمی معتبر بدون ارقام تکراری وارد می کند. اگر ورودی نامعتبر باشد، از پخش کننده خواسته می شود دوباره امتحان کند.
5. نتیجه:
- در پایان بازی به بازیکن در صورتی که عدد را به درستی حدس زده باشد و یا تلاش هایش تمام شده است به همراه شماره مخفی مطلع می شود.
- این رویکرد ساختاریافته برای کدنویسی امکان درک آسان و توسعه پذیری را فراهم می کند و آن را به نمونه ای عالی از نحوه پیاده سازی منطق بازی در پایتون تبدیل می کند.

## نحوه کار کد (تجزیه گام به گام):
کد ارائه شده یک بازی "بولز و گاو" را پیاده سازی می کند که در آن بازیکن سعی می کند یک عدد چهار رقمی به طور تصادفی تولید شده را بدون تکرار ارقام حدس بزند. در اینجا یک تجزیه و تحلیل دقیق از نحوه عملکرد کد مرحله به مرحله آورده شده است:

1. <b>وارد کردن ماژول مورد نیاز</b>
```python
import random
```
کد با وارد کردن ماژول تصادفی شروع می شود که برای تولید اعداد تصادفی استفاده می شود.

2. <b>عملکرد دریافت رقم</b>
   کد شامل چندین تابع است که اهداف مشخصی را انجام می دهند:<br>
   
- <b>a. getDigits(num)</b>
 ```python
def getDigits(num): 
    return [int(i) for i in str(num)]
```
هدف: این تابع یک عدد صحیح می گیرد و آن را به لیستی از ارقام مجزا تبدیل می کند.
عملکرد: ابتدا عدد به یک رشته تبدیل می شود و امکان تکرار روی هر کاراکتر را فراهم می کند. سپس هر کاراکتر به یک عدد صحیح تبدیل شده و به عنوان یک لیست برگردانده می شود. به عنوان مثال، اگر num 1234 باشد، تابع [1، 2، 3، 4] را برمی گرداند.

- <b>b. noDuplicates(num)</b>
```python
def noDuplicates(num): 
    num_li = getDigits(num) 
    if len(num_li) == len(set(num_li)): 
        return True
    else: 
        return False
```
هدف: این تابع بررسی می کند که آیا یک عدد داده شده دارای ارقام تکراری است یا خیر.
عملکرد: با استفاده از getDigits(num) عدد را به لیستی از ارقام تبدیل می کند و سپس طول این لیست را با طول مجموعه ایجاد شده از آن مقایسه می کند. از آنجایی که مجموعه ها نمی توانند موارد تکراری داشته باشند، عدم تطابق نشان دهنده وجود موارد تکراری است. اگر مورد تکراری یافت نشد، تابع True را برمی‌گرداند، در غیر این صورت False.

- <b>c. generateNum()</b>
```python
def generateNum(): 
    while True: 
        num = random.randint(1000,9999) 
        if noDuplicates(num): 
            return num 
```
هدف: این تابع یک عدد چهار رقمی تصادفی تولید می کند که هیچ رقم تکراری ندارد.
عملکرد: به طور مکرر یک عدد صحیح تصادفی بین 1000 و 9999 تولید می کند. برای هر عدد تولید شده، با استفاده از noDuplicates(num) وجود موارد تکراری را بررسی می کند. هنگامی که یک عدد معتبر پیدا شد، آن عدد را برمی گرداند.

- <b>d. numOfBullsCows(num, guess)</b>
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
<b>هدف:</b> این تابع تعداد گاوها و گاوها را بین عدد مخفی (تعداد) و حدس بازیکن محاسبه می کند.(guess).

<b>عملکرد:</b>
یک لیست bull_cow را برای پیگیری گاو نر (رقم صحیح در موقعیت صحیح) و گاو (رقم صحیح در موقعیت اشتباه) مقداردهی اولیه می کند.
ارقام هر دو عدد مخفی و حدس با استفاده از getDigits () استخراج می شوند.
سپس تابع از طریق ارقام هر دو لیست تکرار می شود. برای هر رقم، بررسی می کند که آیا رقم موجود در حدس در شماره مخفی وجود دارد یا خیر.
اگر یک رقم از نظر ارزش و موقعیت مطابقت داشته باشد، به عنوان یک گاو نر حساب می شود. اگر فقط از نظر ارزش مطابقت داشته باشد، به عنوان یک گاو محسوب می شود.
در نهایت، تابع تعداد گاوها و گاوها را برمی گرداند.

3. <b>راه اندازی اولیه بازی</b>
```python
num = generateNum() 
tries = int(input('Enter number of tries: ')) 
count = 0
```
<b>هدف:</b> بازی با ایجاد یک عدد مخفی با استفاده از ()geneNum شروع می شود. از بازیکن خواسته می‌شود تعداد تلاش‌هایی را که می‌خواهند برای حدس زدن عدد وارد کنند، و یک شمارنده (شمارش) برای پیگیری تعداد حدس‌های انجام‌شده مقداردهی اولیه می‌شود.

4. <b>حلقه بازی</b>
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

5. <b>نتیجه گیری:</b>
    این اجرای بازی Bulls and Cows چندین مفهوم مهم برنامه نویسی را به نمایش می گذارد، مانند:<br>
	توابع: کپسوله کردن رفتار در بلوک های قابل استفاده مجدد.<br>
	حلقه ها: استفاده از حلقه ها برای اجازه دادن به تعامل مکرر تا زمانی که یک شرط برآورده شود.<br>
	شرایط: اجرای منطق شرطی برای هدایت جریان برنامه بر اساس ورودی کاربر و قوانین بازی.


## بهبودهای بالقوه
رابط کاربری: بازی را می توان با یک رابط کاربری گرافیکی (GUI) برای بهبود تجربه کاربر بهبود بخشید.<br>
سیستم امتیازدهی: پیاده‌سازی یک سیستم امتیازدهی بر اساس تعداد تلاش‌ها می‌تواند لایه دیگری از رقابت را اضافه کند.<br>
سطوح دشواری چندگانه: معرفی طول‌های مختلف اعداد (مثلاً 3، 4 یا 5 رقم) می‌تواند به بازیکنانی با سطوح مختلف مهارت پاسخ دهد.<br>
تاریخچه بازی: پیگیری حدس‌های قبلی و ارائه بازخورد می‌تواند به بازیکنان در استراتژی‌بندی حدس‌هایشان کمک بیشتری کند.<br>

## کتابخانه های مورد استفاده
تصادفی: برای تولید اعداد تصادفی.<br>
json: در حالی که کتابخانه json وارد شده است، در این کد از آن استفاده نمی شود. اگر قصد دارید بازی را برای ذخیره یا بارگیری حالت های بازی گسترش دهید، می تواند مفید باشد.<br>

این تجزیه و تحلیل دقیق می تواند برای مستندسازی یا آپلود در GitHub استفاده شود و به کاربران کمک کند ساختار، عملکرد و پیشرفت های بالقوه کد را درک کنند.


## کد پایتون
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

