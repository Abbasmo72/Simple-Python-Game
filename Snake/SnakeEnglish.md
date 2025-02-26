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
When the game ends, a retry and exit option appears.
```python
pygame.draw.rect(screen, GREEN, [WIDTH / 3, HEIGHT / 2, 100, 50])
pygame.draw.rect(screen, RED, [WIDTH / 2, HEIGHT / 2, 100, 50])
show_message("Retry", BLACK, [WIDTH / 3 + 20, HEIGHT / 2 + 10])
show_message("Exit", BLACK, [WIDTH / 2 + 30, HEIGHT / 2 + 10])
```
- Clicking Retry restarts the game.
- Clicking Exit closes the application.
## Improvements & Future Enhancements
📌 Add Difficulty Levels – Implement different speeds based on user selection.<br>
📌 Add Power-Ups – Introduce special items that increase/decrease the snake’s size.<br>
📌 Implement a Leaderboard – Store the best scores in a file for persistent tracking.<br>
📌 Multiplayer Mode – Allow two players to control different snakes.<br>
## Conclusion
This project provides a fun and engaging Snake Game using Python and Pygame. The game successfully integrates movement mechanics, collision detection, and score tracking. Future improvements can make the game even more exciting! 🚀
## Python Code
```python
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
GRAY = (200, 200, 200)
BORDER_COLOR = (150, 0, 0)

# Screen dimensions
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 10
SPEED = 7  # Adjusted snake speed

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font settings
font = pygame.font.SysFont("bahnschrift", 25)

# Score variables
score = 0
best_score = 0

def draw_snake(block_size, snake_list):
    """Draw the snake on the screen."""
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, [block[0], block[1], block_size, block_size])

def show_message(msg, color, position):
    """Display a message on the screen."""
    message = font.render(msg, True, color)
    screen.blit(message, position)

def draw_grid():
    """Draw a grid on the game board."""
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def game_loop():
    """Main game loop."""
    global score, best_score
    game_over = False
    game_close = False

    # Initial snake position
    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    # Initial food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
    
    clock = pygame.time.Clock()
    
    while not game_over:
        while game_close:
            # Display game over screen
            screen.fill(WHITE)
            show_message(f"Game Over! Score: {score}", RED, [WIDTH / 3, HEIGHT / 3])
            pygame.draw.rect(screen, GREEN, [WIDTH / 3, HEIGHT / 2, 100, 50])
            pygame.draw.rect(screen, RED, [WIDTH / 2, HEIGHT / 2, 100, 50])
            show_message("Retry", BLACK, [WIDTH / 3 + 20, HEIGHT / 2 + 10])
            show_message("Exit", BLACK, [WIDTH / 2 + 30, HEIGHT / 2 + 10])
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if WIDTH / 3 <= mouse_x <= WIDTH / 3 + 100 and HEIGHT / 2 <= mouse_y <= HEIGHT / 2 + 50:
                        game_loop()
                    if WIDTH / 2 <= mouse_x <= WIDTH / 2 + 100 and HEIGHT / 2 <= mouse_y <= HEIGHT / 2 + 50:
                        game_over = True
                        game_close = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                # Handle movement keys
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

        # Check if snake hits the border
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        screen.fill(WHITE)
        draw_grid()
        
        # Draw border
        pygame.draw.rect(screen, BORDER_COLOR, [0, 0, WIDTH, BLOCK_SIZE])  # Top
        pygame.draw.rect(screen, BORDER_COLOR, [0, HEIGHT - BLOCK_SIZE, WIDTH, BLOCK_SIZE])  # Bottom
        pygame.draw.rect(screen, BORDER_COLOR, [0, 0, BLOCK_SIZE, HEIGHT])  # Left
        pygame.draw.rect(screen, BORDER_COLOR, [WIDTH - BLOCK_SIZE, 0, BLOCK_SIZE, HEIGHT])  # Right
        
        # Draw food
        pygame.draw.rect(screen, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake collides with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        show_message(f"Score: {score}", BLUE, [10, 10])
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1
            score += 10
            if score > best_score:
                best_score = score

        clock.tick(SPEED)
    
    pygame.quit()
    quit()

game_loop()

```

