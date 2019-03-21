import os

import pygame
from pygame.sprite import Sprite

from settings import Settings


class Alien(Sprite):
     """Encapsulates the enemy aliens"""

     def __init__(self, surface, game_settings, x_offset=0, y_offset=0):
          """Initialize a new Alien"""
          super().__init__()
          #Get the image
          self.path = os.path.dirname(__file__)
          img_path = os.path.join(self.path, 'images', 'alien.bmp')
          self.image = pygame.image.load(img_path)
          self.screen = surface
          self.game_settings = game_settings

          #Positioning
          self.rect = self.image.get_rect()
          self.rect.x = self.rect.width*(2*x_offset + 1)
          self.rect.y = self.rect.height*(2*y_offset + 1)
     
          #Movement flags
          self.moving_left = True
          self.moving_down = False
          self.moving_right = False

          self.last_y = self.rect.y

     def blitme(self):
          """Draw an alien to the screen"""
          self.screen.blit(self.image, self.rect)

     def update(self, game_settings):
          """Move the alien left, then down, then right, then down, left, down, right, down..."""
          if self.moving_left:
               self.rect.x -= self.game_settings.alien_speed
               if self.rect.x <= 0:
                    self.moving_left = False
                    self.moving_down = True

          elif self.moving_down:
               self.rect.y += self.game_settings.alien_speed
               if self.last_y + self.game_settings.alien_height <= self.rect.y:
                    self.moving_down = False
                    if self.rect.x == 0:
                         self.moving_right = True
                    elif self.rect.right == self.game_settings.screen_width:
                         self.moving_left = True
                    self.last_y = self.rect.y

          elif self.moving_right:
               self.rect.x += self.game_settings.alien_speed
               if self.rect.right >= self.game_settings.screen_width:
                    self.moving_right = False
                    self.moving_down = True
          if self.rect.y >= 800:
               game_settings.lives -= 1
               self.rect.x = -666
               self.rect.y = -666
               snd_path = os.path.join(self.path, 'audio', 'impact_alarm.mp3')
               pygame.mixer.music.load(snd_path)
               pygame.mixer.music.play()
          self.blitme()