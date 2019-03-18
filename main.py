import pygame

from settings import Settings
import game_functions as gf
from ship import Ship


def run_game():
    """Main game loop"""

    pygame.init()
    gs = Settings()
    screen = pygame.display.set_mode((gs.screen_width, gs.screen_height))
    pygame.display.set_caption("Alien Invasion")

    game_ship = Ship(screen, gs)

    while True:

        gf.check_events(game_ship)
        gf.update_screen(screen, gs, game_ship)


run_game()
