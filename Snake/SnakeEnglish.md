<div align="center">

# Snake
<img src="https://media3.giphy.com/media/uROEXn0SnjTaUcobHi/200w.gif?cid=6c09b952dsxrlsodcdibp0a0445up0qxbx8amkie6yz7r7tw&ep=v1_gifs_search&rid=200w.gif&ct=g" alt="Image Description" width="20%">
</div>
<hr>

[Click to see the descriptions in Persian language](SnakePersian.md)
<hr>

[Python Code](SnakeEnglish.py)

## Overview of the Code
This project is a simple implementation of the classic Snake Game using Python and Pygame. The game provides an interactive environment where the player controls a growing snake that moves across the screen, eats food, and avoids collisions with the walls and itself.

## Features
✅ Smooth Gameplay – The snake moves seamlessly in all four directions.<br>
✅ Score Tracking – Displays the current and best score.<br>
✅ Game Over Screen – Provides options to retry or exit when the snake collides.<br>
✅ Dynamic Food Placement – The food appears at random positions after being eaten.<br>
✅ Grid-Based Movement – The snake moves in fixed blocks for better control.<br>
✅ Border Collision Detection – Ends the game when the snake hits the boundaries.<br>
## Code Breakdown
### 1. Initializing Pygame & Defining Constants
At the beginning of the script, Pygame is initialized, and essential colors, screen dimensions, and snake properties are set.
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
SPEED = 7  # Adjusted snake speed
```
- The game screen size is 600x400 pixels.
- The BLOCK_SIZE determines the size of each segment of the snake.
- SPEED controls the movement speed of the snake.
### 2. Drawing Functions
The game includes functions to draw the snake, display messages, and render the grid.
```python
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, [block[0], block[1], block_size, block_size])
```
- This function iterates through snake_list and draws each segment on the screen.
```python
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))
```
- A grid is drawn to visually align the snake's movement with the screen.
### 3. Main Game Loop
The game_loop() function is the core of the game, handling movement, collision detection, and game logic.
```python
while not game_over:
```
- The game continuously runs until game_over is set to True.

Handling Keyboard Inputs
```python
elif event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        x_change = -BLOCK_SIZE
        y_change = 0
    elif event.key == pygame.K_RIGHT:
        x_change = BLOCK_SIZE
        y_change = 0
    elif event.key == pygame.K_UP:
        y_change = -BLOCK_SIZE
        x_change = 0
    elif event.key == pygame.K_DOWN:
        y_change = BLOCK_SIZE
        x_change = 0
```
- The snake moves left, right, up, or down based on the arrow keys.

Collision with Borders
```python
if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
    game_close = True
```
- If the snake moves out of bounds, the game ends.

Collision with Itself
```python
for segment in snake_list[:-1]:
    if segment == snake_head:
        game_close = True
```
- If the snake collides with itself, the game ends.

Food Consumption
```python
if x == food_x and y == food_y:
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
    snake_length += 1
    score += 10
    if score > best_score:
        best_score = score
```
- When the snake eats food, it grows and the score increases.
## Game Over Screen
