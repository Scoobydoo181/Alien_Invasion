import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from ship import Ship
from alien import Alien

def run_game():
     """Main game loop"""

     #Create window, settings object, and screen
     pygame.init()
     gs = Settings()
     screen = pygame.display.set_mode((gs.screen_width, gs.screen_height))
     pygame.display.set_caption("Alien Invasion") 
    
     #Create ship, bullet list, and alien list
     game_ship = Ship(screen, gs)
     bullet_group = Group()
     alien_group = Group()
     
     #Fill with aliens
     gf.create_fleet(alien_group, screen, gs)

     #Display the controls screen
     gf.show_tutorial(screen)
     
     delay_counter = 0
     while True:
          gf.check_events(game_ship, bullet_group)
          val = gf.update_screen(screen, gs, game_ship, bullet_group, alien_group)

          if val:
               break
               
          if not alien_group:
               if delay_counter >= 250:
                    gs.alien_speed += 1
                    gf.create_fleet(alien_group, screen, gs)
                    delay_counter = 0
               else:
                    delay_counter += 1

     
     end_screen = True
     while end_screen:
          end_screen = gf.game_over(screen, gs)

#Start main loop
run_game()
