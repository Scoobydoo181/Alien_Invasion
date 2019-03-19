from enum import Enum

import pygame
from pygame.sprite import Sprite

class BulletTypes(Enum):
     Ship = 1
     Alien = 2

class Bullet(Sprite):
     """A bullet object that can kill aliens or the ship"""

     def __init__(self, ship):
          """Construct a new bullet sprite"""
          super().__init__()
          self.ship = ship
          self.width = 3
          self.height = 15
          self.color = (60, 60, 60)
          self.speed = 1.1
          self.screen = self.ship.screen
          self.rect = pygame.Rect(ship.rect.left, ship.rect.top, self.width, self.height)

     def move_bullet(self):
          """Increment the bullet's vertical position"""
          self.rect.centery -= round(self.speed)

     def blitme(self):
          """Draw the bullet to the screen"""
          pygame.draw.rect(self.screen, self.color, self.rect)

