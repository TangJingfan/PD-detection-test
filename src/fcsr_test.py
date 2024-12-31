import pygame
import random
import time
import config

# init pygame
pygame.init()

# answer 
items = [
    {"线索": "动物", "关键词": "大象"},
    {"线索": "水果", "关键词": "苹果"},
    {"线索": "交通工具", "关键词": "公交车"},
    {"线索": "颜色", "关键词": "蓝色"}
]
random.shuffle(items)

# 显示文字的函数
def draw_text(text, x, y, color=config.BLACK):
    render = config.normal_font_small.render(text, True, color)
    config.screen.blit(render, (x, y))

# 主测试流程
def memory_test():
    running = True
    stage = "learning"
    current_index = 0
    user_input = ""
    recall_results = []
    free_recall_results = []
    correct_recall = 0

    while running:
        config.screen.fill(config.WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.TEXTINPUT:
                user_input += event.text
            elif event.type == pygame.KEYDOWN:
                if stage in ["free_recall", "recall"]:
                    if event.key == pygame.K_RETURN:
                        if stage == "free_recall":
                            free_recall_results.append(user_input.strip())
                        elif stage == "recall":
                            recall_results.append(user_input.strip())
                        user_input = ""
                        current_index += 1
                        if current_index >= len(items):
                            if stage == "free_recall":
                                stage = "recall"
                                current_index = 0
                            else:
                                stage = "results"
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]

        if stage == "learning":
            if current_index < len(items):
                cue = items[current_index]["线索"]
                item = items[current_index]["关键词"]
                draw_text(f"线索: {cue} - 关键词: {item}", 200, 250)
                pygame.display.flip()
                time.sleep(2)
                current_index += 1
            else:
                stage = "free_recall"
                current_index = 0

        elif stage == "free_recall":
            draw_text("自由回忆阶段: 输入你记得的所有项目并按回车确认。", 50, 200)
            draw_text(f"你的答案: {user_input}", 50, 300)
            pygame.display.flip()

        elif stage == "recall":
            if current_index < len(items):
                cue = items[current_index]["线索"]
                draw_text(f"提示回忆阶段: 根据线索回答。", 50, 200)
                draw_text(f"线索: {cue}", 200, 250)
                draw_text(f"你的答案: {user_input}", 200, 300)
            pygame.display.flip()

        elif stage == "results":
            # 计算自由回忆正确数量
            free_recall_correct = len(set(free_recall_results).intersection(set([item['关键词'] for item in items])))
            # 计算提示回忆正确数量
            cued_recall_correct = sum(1 for i, result in enumerate(recall_results) if result.lower() == items[i]["关键词"].lower())
            # 计算两个环节都正确的数量
            both_correct = len(set(free_recall_results).intersection(set(result for i, result in enumerate(recall_results) if result.lower() == items[i]["关键词"].lower())))

            for i, result in enumerate(recall_results):
                correct = "正确" if result.lower() == items[i]["关键词"].lower() else "不正确"
                draw_text(f"线索: {items[i]['线索']}, 你的答案: {result}, 结果: {correct}", 50, 100 + i * 30)

            draw_text(f"自由回忆阶段任务结果: {free_recall_correct}/{len(items)} 正确", 50, 400, config.BLUE)
            draw_text(f"提示回忆阶段任务结果: {cued_recall_correct}/{len(items)} 正确", 50, 450, config.BLUE)
            draw_text(f"两次回忆都正确: {both_correct}/{len(items)}", 50, 500, config.BLUE)
            pygame.display.flip()
            time.sleep(5)
            running = False

        pygame.display.flip()

    pygame.quit()

# 运行测试
if __name__ == "__main__":
    memory_test()
