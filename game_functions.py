import sys

import pygame

from bullet import Bullet


def check_events(ship, bullet_group):
        """Check for and respond to any game events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                bullet_group.add(Bullet(ship))
                check_movement_event(event,ship)


def update_screen(screen, settings, ship, bullet_group):
        """Refresh the screen and redraw all sprites"""
        screen.fill(settings.bg_color)
        ship.move_ship()
        ship.blitme()
        for bullet in bullet_group:
                bullet.move_bullet()
                bullet.blitme()
        remove_bullets(bullet_group)
        pygame.display.flip()

def remove_bullets(bullet_group):
        """Remove bullets that exit the screen"""
        for bullet in bullet_group.copy():
                if bullet.rect.centery <= 0:
                        bullet_group.remove(bullet)

def check_movement_event(event, ship):
        """Check for keypress events that cause movement"""
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        ship.moving_right = True
                elif event.key == pygame.K_LEFT  or event.key == pygame.K_a:
                        ship.moving_left = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        ship.moving_up = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        ship.moving_down = True

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        ship.moving_right = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        ship.moving_left = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        ship.moving_up = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        ship.moving_down = False