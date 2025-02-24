import pygame
import time
import random

# تنظیمات اولیه
pygame.init()

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
GRAY = (200, 200, 200)
BORDER_COLOR = (150, 0, 0)

# ابعاد صفحه
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 10
SPEED = 7  # کاهش بیشتر سرعت حرکت مار

# نمایش صفحه بازی
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# فونت
font = pygame.font.SysFont("bahnschrift", 25)

# امتیاز
score = 0
best_score = 0

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, [block[0], block[1], block_size, block_size])

def show_message(msg, color, position):
    message = font.render(msg, True, color)
    screen.blit(message, position)

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def game_loop():
    global score, best_score
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
    
    clock = pygame.time.Clock()
    
    while not game_over:
        while game_close:
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

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        screen.fill(WHITE)
        draw_grid()
        pygame.draw.rect(screen, BORDER_COLOR, [0, 0, WIDTH, BLOCK_SIZE])  # بالا
        pygame.draw.rect(screen, BORDER_COLOR, [0, HEIGHT - BLOCK_SIZE, WIDTH, BLOCK_SIZE])  # پایین
        pygame.draw.rect(screen, BORDER_COLOR, [0, 0, BLOCK_SIZE, HEIGHT])  # چپ
        pygame.draw.rect(screen, BORDER_COLOR, [WIDTH - BLOCK_SIZE, 0, BLOCK_SIZE, HEIGHT])  # راست
        pygame.draw.rect(screen, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        show_message(f"Score: {score}", BLUE, [10, 10])
        pygame.display.update()

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
