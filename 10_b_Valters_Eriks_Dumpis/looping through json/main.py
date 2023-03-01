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
color = (0, 0, 255)

while True:
    
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:           
            if event.key in [pygame.K_w, pygame.K_UP]:
                snake_y -= 20
            elif event.key in [pygame.K_s, pygame.K_DOWN]:
                snake_y += 20
            elif event.key in [pygame.K_a, pygame.K_LEFT]:
                snake_x -= 20
            elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                snake_x += 20

    snake = pygame.Rect(snake_x, snake_y, 20, 20)
    pygame.draw.rect(window, (0, 150, 150), snake)
    pygame.display.update()