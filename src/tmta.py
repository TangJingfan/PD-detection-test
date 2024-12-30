import pygame
import random
import config
import time

pygame.init()

CIRCLE_RADIUS = int(config.screen_width / 40)
CIRCLE_PADDING = 80

def generate_positions():
    positions = []
    while len(positions) < 25:
        x = random.randint(CIRCLE_PADDING, config.screen_width - CIRCLE_PADDING)
        y = random.randint(CIRCLE_PADDING, config.screen_height - CIRCLE_PADDING)
        if all((x - px) ** 2 + (y - py) ** 2 >= (CIRCLE_RADIUS * 2) ** 2 for px, py in positions):
            positions.append((x, y))
    return positions

def tmta_test():
    running = True
    start_time = None
    errors = 0
    next_number = 1
    positions = generate_positions()
    clicked = [False] * 25

    while running:
        config.screen.fill(config.WHITE)

        # 绘制圆圈
        for i, (x, y) in enumerate(positions):
            color = config.RED if clicked[i] else (config.GREEN if i + 1 == next_number else config.BLUE)
            pygame.draw.circle(config.screen, color, (x, y), CIRCLE_RADIUS)
            text = config.normal_font_small.render(str(i + 1), True, config.WHITE)
            config.screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

        # 检测事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                for i, (x, y) in enumerate(positions):
                    if not clicked[i] and (x - mx) ** 2 + (y - my) ** 2 <= CIRCLE_RADIUS ** 2:
                        if i + 1 == next_number:
                            clicked[i] = True
                            next_number += 1
                            if next_number > 25:
                                running = False
                                end_time = time.time()
                        else:
                            errors += 1

        pygame.display.update()

    # 结果页面
    duration = round(end_time - start_time, 2) if start_time else 0
    while True:
        config.screen.fill(config.WHITE)
        result_text = config.normal_font_big.render(f"完成时间: {duration} 秒", True, config.BLACK)
        error_text = config.normal_font_big.render(f"错误点击: {errors} 次", True, config.BLACK)
        config.screen.blit(result_text, (config.screen_width // 2 - result_text.get_width() // 2, config.screen_height // 2 - 40))
        config.screen.blit(error_text, (config.screen_width // 2 - error_text.get_width() // 2, config.screen_height // 2 + 20))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
