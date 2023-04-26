import pygame
import random

# initialize Pygame
pygame.init()

# set screen dimensions
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mini Baseball Game")

# set up colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (50,205,50)

# set up fonts
font = pygame.font.Font(None, 30)

# set up game variables
inning = 1
home_score = 0
away_score = 0
outs = 0
strikes = 0
balls = 0
pitch_count = 0
pitch_types = ["Fastball", "Sinker", "Curve", "Slider"]
player_positions = {"home": (screen_width // 2, screen_height - 50),
                    "first": (50, screen_height // 2),
                    "second": (screen_width // 2, 50),
                    "third": (screen_width - 50, screen_height // 2)}

# set up player positions
home_player_pos = player_positions["home"]
away_player_pos = player_positions["first"]
runner_on_first = False
runner_on_second = False
runner_on_third = False

# set up game loop
game_running = True
clock = pygame.time.Clock()

while game_running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # check if the ball is hit
                if home_player_pos == player_positions["first"] and away_player_pos == player_positions["home"]:
                    if random.choice([True, False]):
                        if runner_on_third:
                            away_score += 1
                            runner_on_third = False
                        if runner_on_second:
                            runner_on_third = True
                            runner_on_second = False
                        if runner_on_first:
                            runner_on_second = True
                            runner_on_first = False
                        away_player_pos = player_positions["home"]
                    else:
                        if strikes < 2:
                            strikes += 1
                        else:
                            strikes = 0
                            outs += 1
                            if outs == 3:
                                if inning < 3:
                                    inning += 1
                                    home_player_pos = player_positions["home"]
                                    away_player_pos = player_positions["first"]
                                    runner_on_first = False
                                    runner_on_second = False
                                    runner_on_third = False
                                    outs = 0
                                    strikes = 0
                                    balls = 0
                                    pitch_count = 0
                                    pitch_type = ""
                                else:
                                    game_running = False
                                    print("Final Score:")
                                    print("Home: {}".format(home_score))
                                    print("Away: {}".format(away_score))
                else:
                    if home_player_pos == player_positions["home"]:
                        home_player_pos = player_positions["first"]
                    elif home_player_pos == player_positions["first"] and away_player_pos == player_positions["second"]:
                        home_score += 1
                        home_player_pos = player_positions["home"]
                        runner_on_second = False
                    elif home_player_pos == player_positions["first"] and away_player_pos == player_positions["third"]:
                        home_score += 1
                        home_player_pos = player_positions["home"]
                        runner_on_third = False
                    elif home_player_pos == player_positions["first"]:
                        runner_on_first = True
                        home_player_pos = player_positions
