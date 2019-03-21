import os

import pygame


class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2.5
        self.alien_speed = 1
        self.score = 0
        self.lives = 3
        self.death_safety_counter = 200

        path = os.path.dirname(__file__)
        path = os.path.join(path, 'images', 'alien.bmp')
        image = pygame.image.load(path)

        self.alien_width = image.get_rect().width
        self.alien_height = image.get_rect().height

    def change_score(self, score_change):
        self.score += score_change
