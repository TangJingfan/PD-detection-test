import pygame
from button import Button
import config

pygame.init()

def show_tmta_illustration():
    tmta_illustration = True
    button = Button("继续", (config.screen_width / 2 - 50), int(3 / 4 * config.screen_height), 2 * int(config.screen_width / 25 * 7 / 10), int(config.screen_width / 25 * 7 / 10), config.TIMBERWOLF, config.BLACK, config.bold_font_small)

    while tmta_illustration:
        config.screen.fill(config.WHITE)

        task_text = config.bold_font_big.render("在接下来的任务中", True, config.BLACK)
        illustration_text = config.bold_font_big.render("请按照数字由小到大的顺序", True, config.BLACK)
        illustration_text_2 = config.bold_font_big.render("点击数字对应的圆圈", True, config.BLACK)
        start_text = config.bold_font_big.render("请点击按钮后继续测试", True, config.BLACK)

        config.screen.blit(task_text, (config.screen.get_width() // 2 - task_text.get_width() // 2, config.screen.get_height() // 4))
        config.screen.blit(illustration_text, (config.screen.get_width() // 2 - illustration_text.get_width() // 2, config.screen.get_height() // 4 + config.screen.get_height() // 15))
        config.screen.blit(illustration_text_2, (config.screen.get_width() // 2 - illustration_text_2.get_width() // 2, config.screen.get_height() // 4 + 2 * config.screen.get_height() // 15))
        config.screen.blit(start_text, (config.screen.get_width() // 2 - start_text.get_width() // 2, config.screen.get_height() // 4 + 3 * config.screen.get_height() // 15))

        button.draw(config.screen)

        
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    tmta_illustration = False

        pygame.display.update()
