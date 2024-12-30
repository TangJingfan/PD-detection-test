import pygame

# init pygame
pygame.init()

# set size
# get screen resolution
screen_info = pygame.display.Info()
screen_width, screen_height = int(3 / 4 * screen_info.current_w), int(3 / 4 * screen_info.current_h)

# define color set for test
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_GREY = (50, 50, 50)
LIGHT_GREY = (200, 200, 200)
TIMBERWOLF = (216, 212, 213)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# import chinese font
normal_font_big = pygame.font.Font("font/normal.TTF", int(screen_width / 30))
normal_font_small = pygame.font.Font("font/normal.TTF", int(screen_width / 30 * 7 / 10))
bold_font_big = pygame.font.Font("font/bold.TTF", int(screen_width / 30))
bold_font_small = pygame.font.Font("font/bold.TTF", int(screen_width / 30 * 7 / 10))

# set the size of the window
screen = pygame.display.set_mode((screen_width, screen_height))