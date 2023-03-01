import pygame
import random

pygame.init()

window = pygame.display.set_mode([480, 715])
pygame.display.set_caption('pilnÄ«gs kosmoss')

BACKGROUND = pygame.image.load('stars.jpg')
SPACESHIP = pygame.image.load('spaceship.png')
ASTEROID = pygame.image.load('asteroid.png')
MISSILE = pygame.image.load('missile.png')

FONT = pygame.font.SysFont('couriernew', 24)

CREATE_ASTEROID = pygame.USEREVENT
pygame.time.set_timer(CREATE_ASTEROID, 175)

spaceship_x = 217
spaceship_y = 600

spaceship_x_change = 0
spaceship_y_change = 0

spaceship_speed = 0.2

asteroids_coords = []
missiles_coords = []

health = 100
score = 0

while True:

    events = pygame.event.get()

    for event in events:
        
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                spaceship_y_change = -spaceship_speed
                spaceship_x_change = 0

            elif event.key == pygame.K_a:
                spaceship_y_change = 0
                spaceship_x_change = -spaceship_speed

            elif event.key == pygame.K_s:
                spaceship_y_change = spaceship_speed
                spaceship_x_change = 0

            elif event.key == pygame.K_d:
                spaceship_y_change = 0
                spaceship_x_change = spaceship_speed

            elif event.key == pygame.K_SPACE:
                missile_x = spaceship_x + (SPACESHIP.get_width() / 2)
                missile_y = spaceship_y - MISSILE.get_height()

                missiles_coords.append([missile_x, missile_y])

        if event.type == CREATE_ASTEROID:
            asteroid_x = random.randint(20, 430)
            asteroid_y = random.randint(10, 50)

            asteroids_coords.append([asteroid_x, asteroid_y])

    if spaceship_x <= 0 or spaceship_x >= 416:
        spaceship_x_change = -spaceship_x_change

    if spaceship_y <= 0 or spaceship_y >= 651:
        spaceship_y_change = -spaceship_y_change

    spaceship_x += spaceship_x_change
    spaceship_y += spaceship_y_change

    window.blit(BACKGROUND, [0, 0])
    window.blit(SPACESHIP, [spaceship_x, spaceship_y])
 
    text = FONT.render(f'HEALTH: {health}', True, [255, 192, 203])
    window.blit(text, [10, 10])

    text_2 = FONT.render(f'SCORE: {score}', True, [255, 192, 203])
    window.blit(text_2, [10, 30])

    for m_coords in missiles_coords:
        m_coords[1] -= 0.8
        window.blit(MISSILE, m_coords)

        if m_coords[1] < -50:
            missiles_coords.remove(m_coords)

    asteroid_rect = ASTEROID.get_rect()
    missile_rect = MISSILE.get_rect()
    
    spaceship_rect = SPACESHIP.get_rect()
    spaceship_rect.topleft = [spaceship_x, spaceship_y]

    for a_coords in asteroids_coords:
        a_coords[1] += 0.5
        window.blit(ASTEROID, a_coords)

        if a_coords[1] > 720:
            asteroids_coords.remove(a_coords)

        asteroid_rect.topleft = a_coords

        if spaceship_rect.colliderect(asteroid_rect):
            health -= 15
            asteroids_coords.remove(a_coords)

            if health <= 0:
                pygame.quit()

        for m_coords in missiles_coords:
            missile_rect.topleft = m_coords

            if asteroid_rect.colliderect(missile_rect):
                score += 1
                
                asteroids_coords.remove(a_coords)
                missiles_coords.remove(m_coords)

    pygame.display.update()