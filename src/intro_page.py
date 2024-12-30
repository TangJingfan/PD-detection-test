import pygame
from button import Button
import config

# init pygame
pygame.init()

def show_intro_page():
    intro_page = True
    # render button
    button = Button("继续", 350, 400, 100, 50, config.TIMBERWOLF, config.BLACK, config.bold_font_small)

    while intro_page:
        # make the whole screen white
        config.screen.fill(config.WHITE)
        
        # render the title and other texts
        test_name_text = config.bold_font_big.render("帕金森病诊断评估测试", True, config.BLACK)
        illustration_text = config.bold_font_small.render("在测试中，您将完成4个任务", True, config.BLACK)
        start_text = config.bold_font_small.render("请点击按钮后继续测试", True, config.BLACK)

        # position the texts
        config.screen.blit(test_name_text, (config.screen.get_width() // 2 - test_name_text.get_width() // 2, config.screen.get_height() // 4))
        
        # Put new texts below the first text
        config.screen.blit(illustration_text, (config.screen.get_width() // 2 - illustration_text.get_width() // 2, config.screen.get_height() // 4 + 100))
        config.screen.blit(start_text, (config.screen.get_width() // 2 - start_text.get_width() // 2, config.screen.get_height() // 4 + 160))

        # draw the button
        button.draw(config.screen)
        
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    intro_page = False

        pygame.display.update()
