import sys

import pygame


def check_events(ship):
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                                ship.moving_right = True
                        elif event.key == pygame.K_LEFT:
                                ship.moving_left = True
                        elif event.key == pygame.K_UP:
                                ship.moving_up = True
                        elif event.key == pygame.K_DOWN:
                                ship.moving_down = True

                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                                ship.moving_right = False
                        elif event.key == pygame.K_LEFT:
                                ship.moving_left = False
                        elif event.key == pygame.K_UP:
                                ship.moving_up = False
                        elif event.key == pygame.K_DOWN:
                                ship.moving_down = False


def update_screen(screen, settings, ship):

        screen.fill(settings.bg_color)
        ship.blitme()
        ship.move_ship()
        pygame.display.flip()
