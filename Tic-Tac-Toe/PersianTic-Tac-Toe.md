<div align="center">

# بازی دوز
<img alt="Gif" src="https://bartvwezel.nl/wp-content/uploads/2020/09/ezgif.com-video-to-gif-8.gif" height="250px" width="300px">
</div>
<hr>

[Click to see the descriptions in English language](EnglishTic-Tac-Toe.md)
<hr>



## بررسی اجمالی کد
[Python Code](Tic-Tac-Toe/Tic-Tac-Toe.py)

این کد پایتون یک رابط کاربری گرافیکی ساده (GUI) را برای یک بازی Tic-Tac-Toe با استفاده از کتابخانه Tkinter پیاده سازی می کند. این بازی به یک بازیکن انسانی اجازه می دهد تا در برابر حریف هوش مصنوعی بازی کند. در اینجا یک نمای کلی از کد وجود دارد که به اجزای اصلی تقسیم شده است:

1. واردات:
   - <b>tkinter:</b> ابزارهایی را برای ایجاد برنامه های رابط کاربری گرافیکی فراهم می کند.
   - <b>messagebox:</b> کادرهای محاوره ای را برای نمایش پیام ها به کاربر ارائه می دهد.
   - <b>تصادفی:</b> برای تصادفی سازی استفاده می شود (در این کد به صراحت مورد نیاز نیست).

2. توابع منطقی بازی:
   - <b>check_winner(تخته، بازیکن):</b> این تابع با بررسی تمام سطرها، ستون‌ها و مورب‌ها بررسی می‌کند که آیا بازیکن مشخص شده (یا 'X' یا 'O') بازی را برده است.
   - <b>is_board_full(board):</b> بررسی می‌کند که تخته پر است (بدون فضای خالی) تا مشخص کند بازی مساوی است یا خیر.
   - <b>minimax(board, depth, is_maximizing):</b> الگوریتم Minimax را پیاده‌سازی می‌کند که یک تابع بازگشتی است که وضعیت تخته را ارزیابی می‌کند تا بهترین حرکت را برای هوش مصنوعی تعیین کند. بر اساس موقعیت‌های برد، باخت یا تساوی امتیازات را برمی‌گرداند.
   - best_move(board): با ارزیابی تمام حرکات ممکن با استفاده از الگوریتم Minimax و برگرداندن موقعیت حرکت بهینه، بهترین حرکت را برای هوش مصنوعی تعیین می کند.

3. توابع تعامل بازی:
   - <b>make_move(row, col):</b> حرکت بازیکن را با به‌روزرسانی برد و رابط کاربری گرافیکی کنترل می‌کند. بعد از حرکت بازیکن، برد یا تساوی را بررسی می کند و اگر بازی همچنان ادامه دارد، حرکت هوش مصنوعی را فراخوانی می کند.
   - <b>ai_move():</b> حرکت هوش مصنوعی را با استفاده از تابع best_move() اجرا می‌کند، تابلو را به‌روزرسانی می‌کند و پیروزی یا تساوی را بررسی می‌کند.

4. راه اندازی رابط کاربری گرافیکی:
   - یک پنجره Tkinter با عنوان "Tic-Tac-Toe" ایجاد می شود.
   - یک تابلو 3x3 به عنوان لیستی از لیست ها مقداردهی اولیه می شود که نشان دهنده فضاهای خالی است.
   - دکمه هایی برای هر سلول در شبکه ایجاد می شود، با دستوری که با کلیک کردن، تابع make_move را فعال می کند. هر دکمه رابط کاربری گرافیکی را به روز می کند تا نماد پخش کننده فعلی را نشان دهد ("X" برای بازیکن انسانی، "O" برای هوش مصنوعی).

5. حلقه اصلی:
   - root.mainloop() حلقه رویداد Tkinter را شروع می کند و به رابط کاربری گرافیکی اجازه می دهد تا به اقدامات کاربر پاسخ دهد و به روز رسانی ها را نمایش دهد.

### ویژگی های کلیدی
  - بازیکن انسان به عنوان "X" بازی می کند و با کلیک کردن روی دکمه ها حرکت می کند.
  - هوش مصنوعی به عنوان "O" بازی می کند و به طور خودکار حرکات خود را با استفاده از الگوریتم Minimax محاسبه می کند.
  - بازی با یک پیام برد برای بازیکن یا هوش مصنوعی یا یک پیام تساوی زمانی که تخته بدون برنده پر است به پایان می رسد.
  - مدیریت خطا برای مدیریت حرکات نامعتبر گنجانده شده است.

این پیاده سازی یک مثال ساده از استفاده از رابط کاربری گرافیکی برای ایجاد یک بازی تعاملی است که هم تعامل کاربر و هم منطق اولیه هوش مصنوعی را به نمایش می گذارد.

## چگونه کد کار می کند (تجزیه گام به گام):

1. Importing Libraries
```python
import tkinter as tk #provides a library of basic elements of GUI widgets
from tkinter import messagebox #provides a different set of dialogues that are used to display message boxes
import random
```
   - <b>tkinter:</b> این کتابخانه برای ایجاد یک رابط کاربری گرافیکی (GUI) و عناصر مختلف آن استفاده می شود.
   - <b>جعبه پیام:</b> این ماژول به نمایش دیالوگ ها برای نمایش پیام ها به کاربر (مانند پیام های برد یا خطا) کمک می کند.
   - <b>تصادفی:</b> این ماژول برای تصادفی سازی استفاده می شود، اگرچه در کد فعلی استفاده نشده است.

2. تعریف تابع check_winner
```python
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
```
   -این تابع پر بودن برد را بررسی می کند (یعنی فضای خالی وجود ندارد). 
   - از لیست های تودرتو برای بررسی تمام سلول ها استفاده می کند.
   - اگر تمام سلول ها پر شوند، True را برمی گرداند. در غیر این صورت، غلط را برمی گرداند.

4. تعریف تابع minimax
```python
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)
```
   - این تابع پر بودن برد را بررسی می کند (یعنی فضای خالی وجود ندارد).
   - از لیست های تودرتو برای بررسی تمام سلول ها استفاده می کند.
   - اگر تمام سلول ها پر شوند، True را برمی گرداند. در غیر این صورت، False را برمی گرداند.

4. تعریف تابع minimax
```python
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if is_board_full(board): #if game is full, terminate
        return 0

    if is_maximizing: #recursive approach that fills board with Os
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False) #recursion
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else: #recursive approach that fills board with Xs
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True) #recursion
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval
```
   - این تابع الگوریتم Minimax مورد استفاده برای محاسبه بهترین حرکت را پیاده سازی می کند.
   - ابتدا بررسی می کند که آیا یک برنده وجود دارد یا خیر و امتیاز مربوطه را برمی گرداند (-1 برای 'X' و 1 برای 'O').
   - اگر تخته پر باشد، نمره 0 را برمی گرداند.
   - اگر نوبت به هوش مصنوعی برسد (is_maximizing)، تمام حرکات ممکن را برای یافتن بهترین امتیاز ارزیابی می کند.
   - اگر نوبت به بازیکن انسان برسد، امتیاز حرکات را محاسبه می کند تا امتیاز را به حداقل برساند.

5. تعریف تابع best_move
```python
def best_move(board):
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move
```
   - این تابع بهترین حرکت را برای هوش مصنوعی پیدا می کند.
   - تمام حرکات ممکن (سلول های خالی) را ارزیابی می کند تا بهترین امتیاز را با استفاده از Minimax تعیین کند.
   - بهترین حرکت را برمی گرداند (به صورت چند تایی سطر و ستون).

6. تعریف تابع make_move
```python
def make_move(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        buttons[row][col].config(text='X')
        if check_winner(board, 'X'):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            root.quit()
        elif is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            root.quit()
        else:
            ai_move()
    else:
        messagebox.showerror("Error", "Invalid move")
```
   - این عملکرد حرکت بازیکن را مدیریت می کند.
   - ابتدا بررسی می کند که سلول خالی است یا خیر.
   - اگر خالی باشد، "X" را در آن سلول قرار می دهد و نمایشگر را به روز می کند.
   - سپس بررسی می کند که آیا بازیکن برنده شده است یا اینکه تخته پر است و در صورت نیاز پیام های مناسب را نمایش می دهد.
   - اگر بازی ادامه پیدا کند، حرکت هوش مصنوعی را صدا می کند.
   - اگر سلول خالی نباشد پیغام خطا نشان می دهد.

7. تعریف تابع ai_move
```python
def ai_move():
    row, col = best_move(board)
    board[row][col] = 'O'
    buttons[row][col].config(text='O')
    if check_winner(board, 'O'):
        messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
        root.quit()
    elif is_board_full(board):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        root.quit()
```
   - این تابع نوبت هوش مصنوعی را اجرا می کند.
   - بهترین حرکت را با استفاده از best_move محاسبه می کند و "O" را در تابلو قرار می دهد.
   - بررسی می کند که آیا هوش مصنوعی برنده شده است یا اینکه تخته پر است و پیام های مناسب را نمایش می دهد.

8. ایجاد و اجرای رابط کاربری گرافیکی
```python
root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = []

for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text=' ', font=('normal', 30), width=5, height=2, command=lambda row=i, col=j: make_move(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

root.mainloop()
```
   - پنجره اصلی Tkinter ایجاد می شود و عنوان "Tic-Tac-Toe" تنظیم می شود.
   - یک تابلو 3x3 برای نشان دادن وضعیت بازی ایجاد می شود.
   - دکمه هایی برای هر سلول در برد ایجاد می شود و با کلیک بر روی آنها تابع make_move فعال می شود.
   - root.mainloop() حلقه رویداد اصلی را شروع می کند و به برنامه اجازه می دهد به تعاملات کاربر پاسخ دهد.

این کد به طور کامل یک بازی Tic-Tac-Toe را با منطق بازی و یک رابط کاربری گرافیکی پیاده سازی می کند و به بازیکن انسانی اجازه می دهد با یک هوش مصنوعی رقابت کند.

# کد پایتون
```python
import tkinter as tk #provides a library of basic elements of GUI widgets
from tkinter import messagebox #provides a different set of dialogues that are used to display message boxes
import random

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if is_board_full(board): #if game is full, terminate
        return 0

    if is_maximizing: #recursive approach that fills board with Os
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False) #recursion
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else: #recursive approach that fills board with Xs
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True) #recursion
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

#determines the best move for the current player and returns a tuple representing the position
def best_move(board):
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

def make_move(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        buttons[row][col].config(text='X')
        if check_winner(board, 'X'):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            root.quit()
        elif is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            root.quit()
        else:
            ai_move()
    else:
        messagebox.showerror("Error", "Invalid move")

#AI's turn to play
def ai_move():
    row, col = best_move(board)
    board[row][col] = 'O'
    buttons[row][col].config(text='O')
    if check_winner(board, 'O'):
        messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
        root.quit()
    elif is_board_full(board):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        root.quit()

root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = []

for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text=' ', font=('normal', 30), width=5, height=2, command=lambda row=i, col=j: make_move(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

root.mainloop()
```
