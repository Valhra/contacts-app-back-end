import pygame
import random

def random_rgb_color() -> tuple:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


pygame.init()

window = pygame.display.set_mode([800, 600])

snake_x = 200
snake_y = 200

while True:
    
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_y -= 20
            elif event.key == pygame.K_s:
                snake_y += 20
            elif event.key == pygame.K_a:
                snake_x -= 20
            elif event.key == pygame.K_d:
                snake_x += 20
            elif event.key == pygame.K_c:
                window.fill([0, 0, 0])  

    snake = pygame.Rect(snake_x, snake_y, 20, 20)
    pygame.draw.rect(window, random_rgb_color(), snake)
    pygame.display.update() 