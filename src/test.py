import pygame

# 初始化 pygame
pygame.init()

# 设置窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame 中文输入示例")
font = pygame.font.Font(None, 48)  # 使用默认字体
clock = pygame.time.Clock()

# 输入变量
user_input = ""

# 主循环
running = True
while running:
    screen.fill((255, 255, 255))  # 背景颜色
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.TEXTINPUT:
            user_input += event.text  # 收集输入的文本
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]  # 删除最后一个字符
            elif event.key == pygame.K_RETURN:
                print(f"输入的内容: {user_input}")  # 打印输入内容到控制台
                user_input = ""  # 清空输入

    # 渲染用户输入的文本
    text_surface = font.render(user_input, True, (0, 0, 0))
    screen.blit(text_surface, (50, 100))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
