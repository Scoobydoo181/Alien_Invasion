import pygame 

from settings import Settings
import game_functions as gf
from ship import Ship

def run_game():   
    pygame.init()
    gs = Settings()
    screen = pygame.display.set_mode((gs.screen_width, gs.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:
        
        screen.fill(gs.bg_color)
        ship.blitme()
        gf.check_events(ship)
        ship.update()
        pygame.display.update()

run_game()