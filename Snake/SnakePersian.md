<div align="center">

# بازی مار
<img src="https://media3.giphy.com/media/uROEXn0SnjTaUcobHi/200w.gif?cid=6c09b952dsxrlsodcdibp0a0445up0qxbx8amkie6yz7r7tw&ep=v1_gifs_search&rid=200w.gif&ct=g" alt="Image Description" width="20%">
</div>
<hr>

[Click to see the descriptions in English language](SnakeEnglish.md)
<hr>

[کد پایتون](SnakePersian.py)

## معرفی پروژه
این پروژه یک پیاده‌سازی ساده از بازی کلاسیک مار (Snake Game) با استفاده از Pygame است. در این بازی، بازیکن یک مار را کنترل می‌کند که در صفحه حرکت می‌کند، غذا می‌خورد و طول آن افزایش می‌یابد. هدف اصلی این است که تا جای ممکن زنده بمانید و از برخورد با دیوارها و خود مار جلوگیری کنید.
## ویژگی‌های بازی
✅ حرکت روان – مار می‌تواند به چهار جهت حرکت کند.<br>
✅ سیستم امتیازدهی – امتیاز فعلی و بهترین امتیاز نمایش داده می‌شود.<br>
✅ صفحه پایان بازی – امکان شروع مجدد یا خروج از بازی فراهم شده است.<br>
✅ تولید تصادفی غذا – بعد از خورده شدن، غذا در مکان جدیدی ظاهر می‌شود.<br>
✅ حرکت بر اساس شبکه – مار در واحدهای مشخصی حرکت می‌کند که کنترل بازی را آسان‌تر می‌کند.<br>
✅ تشخیص برخورد با دیوارها – اگر مار از صفحه خارج شود، بازی پایان می‌یابد.<br>
## بررسی کد برنامه
۱. مقداردهی اولیه Pygame و تعریف متغیرهای ثابت
در ابتدای کد، Pygame مقداردهی اولیه شده و رنگ‌ها، اندازه صفحه و ویژگی‌های مار تعریف شده‌اند.
```python
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
GRAY = (200, 200, 200)
BORDER_COLOR = (150, 0, 0)

WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 10
SPEED = 7  # سرعت حرکت مار
```
- اندازه صفحه ۶۰۰×۴۰۰ پیکسل است.
- تعیین BLOCK_SIZE اندازه هر بخش از بدن مار را مشخص می‌کند.
- تعیین SPEED سرعت حرکت مار را تعیین می‌کند.

۲. توابع ترسیم مار و صفحه بازی
چند تابع برای کشیدن مار، نمایش پیام‌ها و ترسیم شبکه بازی تعریف شده‌اند.
```python
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, [block[0], block[1], block_size, block_size])
```
- این تابع با استفاده از snake_list تمام بخش‌های مار را روی صفحه نمایش می‌دهد.
```python
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))
```
- این تابع یک شبکه را روی صفحه رسم می‌کند تا حرکت مار دقیق‌تر شود.
