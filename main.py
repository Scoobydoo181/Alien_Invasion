import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from ship import Ship


def run_game():
    """Main game loop"""

    #Create window, settings object, and screen
    pygame.init()
    gs = Settings()
    screen = pygame.display.set_mode((gs.screen_width, gs.screen_height))

    pygame.display.set_caption("Alien Invasion") 

    #Create ship and bullet list
    game_ship = Ship(screen, gs)
    bullet_group = Group()

    while True:
        gf.check_events(game_ship, bullet_group)
        gf.update_screen(screen, gs, game_ship, bullet_group)

#Start main loop
run_game()
