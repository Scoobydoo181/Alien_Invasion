import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
     """A bullet object that can kill aliens or the ship"""

     def __init__(self, ship):
          """Construct a new bullet sprite"""
          super().__init__()
          self.ship = ship
          self.width = 3
          self.height = 15
          self.color = (60, 60, 60)
          self.speed = 1.4
          self.screen = self.ship.screen

          #Create the bullet emerging from the ship
          self.rect = pygame.Rect(ship.rect.left, ship.rect.top, self.width, self.height)

     def move_bullet(self):
          """Increment the bullet's vertical position"""
          self.rect.centery -= round(self.speed)

     def blitme(self):
          """Draw the bullet to the screen"""
          pygame.draw.rect(self.screen, self.color, self.rect)

