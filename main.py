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
    
    gf.create_fleet(alien_group, screen, gs)

    while True:
        gf.check_events(game_ship, bullet_group)
        gf.update_screen(screen, gs, game_ship, bullet_group, alien_group)

#Start main loop
run_game()
