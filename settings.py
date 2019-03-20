import os

import pygame


class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.6

        path = os.path.dirname(__file__)
        path = os.path.join(path, 'images', 'alien.bmp')
        image = pygame.image.load(path)

        self.alien_width = image.get_rect().width
        self.alien_height = image.get_rect().height
