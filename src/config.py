import pygame

screen_height, screen_width = 600, 800

# define color set for test
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# import chinese font
normal_font = pygame.font.Font("font/normal.TTF", 50)
bold_font = pygame.font.Font("font/bold.TTF", 50)

# set the size of the window
screen = pygame.display.set_mode((config.screen_width, config.screen_height))