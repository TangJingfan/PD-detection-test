import pygame

# init pygame
pygame.init()

# set size
screen_height, screen_width = 600, 800

# define color set for test
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_GREY = (50, 50, 50)
LIGHT_GREY = (200, 200, 200)
TIMBERWOLF = (216, 212, 213)

# import chinese font
normal_font_big = pygame.font.Font("font/normal.TTF", 50)
normal_font_small = pygame.font.Font("font/normal.TTF", 35)
bold_font_big = pygame.font.Font("font/bold.TTF", 50)
bold_font_small = pygame.font.Font("font/bold.TTF", 35)

# set the size of the window
screen = pygame.display.set_mode((screen_width, screen_height))