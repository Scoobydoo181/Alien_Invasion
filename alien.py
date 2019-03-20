import os

import pygame
from pygame.sprite import Sprite

from settings import Settings


class Alien(Sprite):
     """Encapsulates the enemy aliens"""

     def __init__(self, surface, x_offset=0, y_offset=0):
          """Initialize a new Alien"""
          super().__init__()

          path = os.path.dirname(__file__)
          path = os.path.join(path, 'images', 'alien.bmp')
          self.image = pygame.image.load(path)
          self.screen = surface

          self.rect = self.image.get_rect()
          self.rect.x = self.rect.width*(2*x_offset + 1)
          self.rect.y = self.rect.height*(2*y_offset +1)

     def blitme(self):
          """Draw an alien to the screen"""
          self.screen.blit(self.image, self.rect)

     
