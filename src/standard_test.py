import pygame
import random
import time
from button import Button 
from intro_page import show_intro_page
import config
from illustration import show_tmta_illustration

# init pygame structure
pygame.init()

# set caption
pygame.display.set_caption("帕金森病诊断评估测试")

def main():
    show_intro_page()
    show_tmta_illustration()

# run main function
if __name__ == "__main__":
    main()

    # quit pygame
    pygame.quit()
