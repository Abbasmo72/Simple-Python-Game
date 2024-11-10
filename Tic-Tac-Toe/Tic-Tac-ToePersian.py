import tkinter as tk # فراهم کردن کتابخانه‌ای برای اجزای اولیه واسط گرافیکی (GUI)
from tkinter import messagebox # فراهم کردن مجموعه‌ای از دیالوگ‌ها برای نمایش پیام‌ها
import random

# تابعی برای بررسی برنده شدن بازیکن (چک کردن سطرها، ستون‌ها و قطرها)
def check_winner(board, player):
    # بررسی برنده شدن بازیکن در هر یک از سطرها یا ستون‌ها
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # بررسی برنده شدن بازیکن در هر یک از قطرها
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# تابعی برای بررسی پر شدن کامل صفحه بازی
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

# الگوریتم Minimax برای پیدا کردن بهترین حرکت
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if is_board_full(board): # اگر بازی پر شود، خاتمه می‌یابد
        return 0

    # حالت حداکثری (پر کردن خانه‌ها با 'O' برای بازیکن کامپیوتر)
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False) # بازگشتی
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    # حالت حداقلی (پر کردن خانه‌ها با 'X' برای بازیکن کاربر)
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True) # بازگشتی
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# تعیین بهترین حرکت برای کامپیوتر، برگشت دادن مختصات آن
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

# تابعی برای انجام حرکت بازیکن و بررسی نتیجه
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

# نوبت حرکت کامپیوتر (AI)
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

# تنظیمات پنجره اصلی بازی
root = tk.Tk()
root.title("Tic-Tac-Toe")

# ساختار اولیه تخته بازی و دکمه‌های هر خانه
board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = []

# ایجاد دکمه‌های ۳x۳ برای تخته بازی
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text=' ', font=('normal', 30), width=5, height=2, command=lambda row=i, col=j: make_move(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

# شروع برنامه اصلی GUI
root.mainloop()
