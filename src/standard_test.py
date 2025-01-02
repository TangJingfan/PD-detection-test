import pygame
from intro_page import show_intro_page
from illustration import show_tmta_illustration, break_time_illustration, show_tmtb_illustration, show_memory_illustration
from tmta import tmta_test
from tmtb import tmtb_test
from fcsr_test import memory_test, typing_test

# init pygame structure
pygame.init()

# set caption
pygame.display.set_caption("帕金森病诊断评估测试")

def main():
    # show_intro_page()
    # show_tmta_illustration()
    # tmta_test()
    # break_time_illustration()
    # show_tmtb_illustration()
    # tmtb_test()
    # break_time_illustration()
    # show_memory_illustration()
    if typing_test():
        memory_test()
    break_time_illustration()

# run main function
if __name__ == "__main__":
    main()

    # quit pygame
    pygame.quit()
