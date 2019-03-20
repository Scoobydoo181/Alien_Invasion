import os

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Implement the player's ship"""

    def __init__(self, screen, settings):
        """Construct a ship at the bottom center of the screen"""
        super().__init__()
        ship_path = os.path.dirname(__file__)
        ship_path = os.path.join(ship_path, 'images', 'ship.bmp')

        self.image = pygame.image.load(ship_path)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.settings = settings

        #Sets position to bottom center
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom
        
        #Movement flags for update loop
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw ship"""
        self.screen.blit(self.image, self.rect)
    
    def move_ship(self):
        """Change the ship's position, stopping the ship if it hits a wall"""
        if self.moving_right:
            if self.rect.right < self.screen.get_rect().right:
                self.rect.centerx += round(self.settings.ship_speed)
            #Allow the ship to leave one edge and enter the other
            if self.rect.right == self.screen.get_rect().right:
                self.rect.centerx = self.screen.get_rect().left

        if self.moving_left:
            if self.rect.left > self.screen.get_rect().left:
                self.rect.centerx -= round(self.settings.ship_speed)
            #Allow the ship to leave one edge and enter the other
            if self.rect.left == self.screen.get_rect().left:
                self.rect.centerx = self.screen.get_rect().right

        max_height = int(self.settings.screen_height*(2/3))
        if self.moving_up:
            if self.rect.top > self.screen.get_rect().top + max_height:
                self.rect.centery -= round(self.settings.ship_speed)

        if self.moving_down:
            if self.rect.bottom < self.screen.get_rect().bottom:
                self.rect.centery += round(self.settings.ship_speed)