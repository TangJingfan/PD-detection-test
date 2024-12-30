import pygame
import random
import config
import time

pygame.init()

CIRCLE_RADIUS = int(config.screen_width / 40)
CIRCLE_PADDING = 80

def generate_positions():
    positions = []
    while len(positions) < 25:  # should be 25
        x = random.randint(CIRCLE_PADDING, config.screen_width - CIRCLE_PADDING)
        y = random.randint(CIRCLE_PADDING, config.screen_height - CIRCLE_PADDING)
        if all((x - px) ** 2 + (y - py) ** 2 >= (CIRCLE_RADIUS * 2) ** 2 for px, py in positions):
            positions.append((x, y))
    return positions

def tmta_test():
    running = True
    next_number = 1
    positions = generate_positions()
    clicked = [False] * 25  # should be 25
    error_count = 0  # Variable to count errors

    # Start the timer
    start_time = time.time()

    # Create transparent canvas to record trajectory
    trajectory_surface = pygame.Surface((config.screen_width, config.screen_height), pygame.SRCALPHA)
    trajectory_surface.fill((0, 0, 0, 0))

    while running:
        config.screen.fill(config.WHITE)

        # Plot circles
        for i, (x, y) in enumerate(positions):
            color = config.GREEN if clicked[i] else config.BLUE
            pygame.draw.circle(config.screen, color, (x, y), CIRCLE_RADIUS)
            text = config.normal_font_small.render(str(i + 1), True, config.WHITE)
            config.screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

        # Track mouse
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(trajectory_surface, config.BLACK + (255,), (mx, my), 5)

        config.screen.blit(trajectory_surface, (0, 0))

        # Detect events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                correct_click = False
                for i, (x, y) in enumerate(positions):
                    if not clicked[i] and (x - mx) ** 2 + (y - my) ** 2 <= CIRCLE_RADIUS ** 2:
                        if i + 1 == next_number:
                            clicked[i] = True
                            next_number += 1
                            correct_click = True
                            if next_number > 25:  # should be 25
                                running = False
                            break
                if not correct_click:
                    error_count += 1  # Increment error count

        pygame.display.update()

    # Calculate total time
    end_time = time.time()
    total_time = end_time - start_time

    # Save trajectory with background, circles, and results
    save_surface = pygame.Surface((config.screen_width, config.screen_height))
    save_surface.fill(config.WHITE)

    # Draw circles on save surface
    for i, (x, y) in enumerate(positions):
        color = config.GREEN if clicked[i] else config.BLUE
        pygame.draw.circle(save_surface, color, (x, y), CIRCLE_RADIUS)
        text = config.normal_font_small.render(str(i + 1), True, config.WHITE)
        save_surface.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    # Overlay the trajectory
    save_surface.blit(trajectory_surface, (0, 0))

    # Add the results text
    time_text = f"Total Time: {total_time:.2f} seconds"
    error_text = f"Errors: {error_count}"

    time_surface = config.normal_font_small.render(time_text, True, config.BLACK)
    error_surface = config.normal_font_small.render(error_text, True, config.BLACK)

    save_surface.blit(time_surface, (10, 10))  # Display time in the top-left corner
    save_surface.blit(error_surface, (10, 60))  # Display errors below the time

    # Save final image
    pygame.image.save(save_surface, "tmt_a_mouse_trajectory.png")
