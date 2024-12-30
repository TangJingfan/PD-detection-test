import pygame

pygame.init()

screen_height, screen_width = 600, 800

# define color set for test
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GREY = (50, 50, 50)

# import chinese font
normal_font = pygame.font.Font("font/normal.TTF", 50)
bold_font = pygame.font.Font("font/bold.TTF", 50)

# set the size of the window
screen = pygame.display.set_mode((screen_width, screen_height))