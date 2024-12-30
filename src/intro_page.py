import pygame
from button import Button
import config

pygame.init()

def show_intro_page():
    intro_page = True
    button = Button("继续", 350, 400, 100, 50, config.LIGHT_GREY, config.WHITE, config.normal_font)

    while intro_page:
        config.screen.fill(config.WHITE)
        text = config.normal_font.render("帕金森病诊断评估测试", True, config.LIGHT_GREY)
        config.screen.blit(text, (config.screen.get_width() // 2 - text.get_width() // 2, config.screen.get_height() // 4))

        button.draw(config.screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    intro_page = False

        pygame.display.update()