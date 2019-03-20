import sys

import pygame
from pygame.sprite import *

from bullet import Bullet
from alien import Alien



def update_screen(screen, settings, ship, bullet_group, alien_group):
        """Refresh the screen and redraw all sprites"""
        #Redraw background color
        screen.fill(settings.bg_color)

        #Update and redraw the ship
        ship.move_ship()
        ship.blitme()

        #Update and redraw bullets
        for bullet in bullet_group:
                bullet.move_bullet()
                bullet.blitme()
        remove_bullets(bullet_group)
        
        #Update and redraw aliens
        for alien in alien_group:
                alien.blitme()

        #Remove dead aliens and bullets
        hit_bullet_group = Group()
        for alien in alien_group.copy():
               hit_bullet_group.add(spritecollide(alien, bullet_group, True))
        for bullet in hit_bullet_group:
                spritecollide(bullet, alien_group, True)
                

        #Redraw whole screen
        pygame.display.flip()

def remove_bullets(bullet_group):
        """Remove bullets that exit the screen"""
        for bullet in bullet_group.copy():
                if bullet.rect.centery <= 0:
                        bullet_group.remove(bullet)

def check_events(ship, bullet_group):
        """Check for and respond to any game events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                        
                check_movement_event(event,ship, bullet_group)

def check_movement_event(event, ship, bullet_group):
        """Check for keypress events that cause movement"""
        check_keydown_event(event, ship, bullet_group)
        check_keyup_event(event, ship)

def check_keydown_event(event, ship, bullet_group):
        """Check if a key was pressed"""
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        ship.moving_right = True
                elif event.key == pygame.K_LEFT  or event.key == pygame.K_a:
                        ship.moving_left = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        ship.moving_up = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                        bullet_group.add(Bullet(ship))

def check_keyup_event(event, ship):
        """Check if a key was released"""
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        ship.moving_right = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        ship.moving_left = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        ship.moving_up = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        ship.moving_down = False

def create_fleet(alien_list, screen, game_settings):
        """Fills one row up with aliens"""
        #Calculate how many aliens can fit on the screen
        available_space = game_settings.screen_width - 2*game_settings.alien_width
        num_aliens = int(available_space /2 )

        #Add the aliens to the group
        for num in range(num_aliens):
                alien_list.add(Alien(screen, num))