import pygame
import config
from tmta import generate_positions, CIRCLE_RADIUS
import time

def tmtb_test():
    running = True
    sequence = ['1', '一', '2', '二', '3', '三', '4', '四', '5', '五', '6', '六', '7', '七', '8', '八']
    next_index = 0
    positions = generate_positions()
    clicked = [False] * len(sequence)
    error_count = 0  # Variable to count errors

    # Start the timer
    start_time = time.time()

    # Create transparent canvas to record trajectory
    trajectory_surface = pygame.Surface((config.screen_width, config.screen_height), pygame.SRCALPHA)
    trajectory_surface.fill((0, 0, 0, 0))

    while running:
        config.screen.fill(config.WHITE)

        # Plot circles
        for i, (x, y) in enumerate(positions[:len(sequence)]):
            color = config.GREEN if clicked[i] else config.BLUE
            pygame.draw.circle(config.screen, color, (x, y), CIRCLE_RADIUS)
            text = config.normal_font_small.render(sequence[i], True, config.WHITE)
            config.screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

        # Track mouse
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(trajectory_surface, config.BLACK + (255,), (mx, my), 2)

        config.screen.blit(trajectory_surface, (0, 0))

        # Detect events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                for i, (x, y) in enumerate(positions[:len(sequence)]):
                    if not clicked[i] and (x - mx) ** 2 + (y - my) ** 2 <= CIRCLE_RADIUS ** 2:
                        if i == next_index:
                            clicked[i] = True
                            next_index += 1
                            if next_index >= len(sequence):
                                running = False
                        else:
                            error_count += 1  # Increment error count for incorrect clicks

        pygame.display.update()

    # Calculate total time
    end_time = time.time()
    total_time = end_time - start_time

    # Save trajectory with background, circles, and time
    save_surface = pygame.Surface((config.screen_width, config.screen_height))
    save_surface.fill(config.WHITE)

    # Draw circles on save surface
    for i, (x, y) in enumerate(positions[:len(sequence)]):
        color = config.GREEN if clicked[i] else config.BLUE
        pygame.draw.circle(save_surface, color, (x, y), CIRCLE_RADIUS)
        text = config.normal_font_small.render(sequence[i], True, config.WHITE)
        save_surface.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    # Overlay the trajectory
    save_surface.blit(trajectory_surface, (0, 0))

    # Add the total time and error count text
    time_text = f"Total Time: {total_time:.2f} seconds"
    error_text = f"Errors: {error_count}"
    time_surface = config.normal_font_small.render(time_text, True, config.BLACK)
    error_surface = config.normal_font_small.render(error_text, True, config.BLACK)
    save_surface.blit(time_surface, (10, 10))  # Display time in the top-left corner
    save_surface.blit(error_surface, (10, 60))  # Display error count below time

    # Save final image
    pygame.image.save(save_surface, "tmt_b_mouse_trajectory.png")
