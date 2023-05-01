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

