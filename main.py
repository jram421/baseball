# file created by jacob ramirez
# https://www.ge.com/digital/documentation/historian/version2022/r_ex_python_additional.html
# https://www.youtube.com/watch?v=0fh_AqXiSHs
# https://www.geeksforgeeks.org/pygame-time/
# https://www.makeuseof.com/pygame-game-scores-displaying-updating/#:~:text=To%20do%20so%2C%20declare%20and,the%20player%20touches%20an%20obstacle.
# https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dot Eater")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (41, 70, 67)

# Set up the fonts
font = pygame.font.SysFont(None, 48)

# Set up the game variables including speed for player, colors, dot sizes and dot spacing
player_pos = [screen_width//2, screen_height//2]
player_size = 20
player_speed = 5
small_dot_size = 10
small_dot_spacing = 50
small_dot_color = green
small_dot_count = 50
small_dots = []
for i in range(small_dot_count):
    small_dots.append([random.randrange(small_dot_size, screen_width-small_dot_size, small_dot_spacing),
                       random.randrange(small_dot_size, screen_height-small_dot_size, small_dot_spacing)])
# Set up the game loop
game_over = False
time_remaining = 30
score = 0
while not game_over:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > player_size:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > player_size:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < screen_height - player_size:
        player_pos[1] += player_speed
    # Handle collisions
    for dot in small_dots:
        distance = ((player_pos[0]-dot[0])**2 + (player_pos[1]-dot[1])**2)**0.5
        if distance < player_size + small_dot_size:
            small_dots.remove(dot)
            score += 1

    # Update the screen
    screen.fill(black)
    for dot in small_dots:
        pygame.draw.circle(screen, small_dot_color, dot, small_dot_size)
    pygame.draw.circle(screen, white, player_pos, player_size)
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, [10, 10])
    time_text = font.render("Time: " + str(time_remaining), True, white)
    screen.blit(time_text, [screen_width - time_text.get_width() - 10, 10])
    pygame.display.flip()

    # Update game variables
    time_remaining -= 1/60
    if time_remaining <= 0:
        game_over = True

    # Wait for the next frame
    clock.tick(60)

# Clean up Pygame
pygame.quit()