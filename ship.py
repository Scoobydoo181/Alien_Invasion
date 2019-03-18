import os
import pygame

class Ship():
    """Implement the player's ship"""

    def __init__(self, screen):
        """Construct a ship at the bottom center of the screen"""
        current_path = os.path.dirname(__file__)
        current_path = os.path.join(current_path, 'images','ship.bmp')

        self.image = pygame.image.load(current_path)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Change the ship's position"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
