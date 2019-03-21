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
        ship.update()
        

        #Update and redraw bullets
        bullet_group.update()
        remove_offscreen_bullets(bullet_group)
        
        #Update and redraw aliens
        alien_group.update()
        
        #Remove dead aliens and bullets
        hit_bullet_group = Group()
        for alien in alien_group:
               hit_bullet_group.add(spritecollide(alien, bullet_group, True))
        for bullet in hit_bullet_group:
                spritecollide(bullet, alien_group, True)
                

        #Redraw whole screen
        pygame.display.flip()

def remove_offscreen_bullets(bullet_group):
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
        """Fills the screen up with aliens"""
        num_aliens = 10
        
        #Add the aliens to the group
        for row in range(4):
                for num in range(num_aliens):
                        alien_list.add(Alien(screen, game_settings, num, row))