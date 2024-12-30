import pygame
import random
import time
from button import Button 
from intro_page import show_intro_page
import config

# init pygame structure
pygame.init()

# set caption
pygame.display.set_caption("帕金森病诊断评估测试")

def main():
    show_intro_page()  # 显示介绍页

# 运行主程序
if __name__ == "__main__":
    main()

    # 退出pygame
    pygame.quit()
