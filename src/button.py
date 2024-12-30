import pygame

class Button:
    # constructor of a button class
    def __init__(self, text, x, y, width, height, color, text_color, font):
        # assignment
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text_color = text_color
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font

    # a member function to draw the button
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        # render text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)