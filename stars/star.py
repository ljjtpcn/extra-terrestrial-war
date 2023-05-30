import pygame

from pygame.sprite import Sprite


class Star(Sprite):
    """星星的类"""

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        """绘制星星"""
        self.screen.blit(self.image, self.rect)