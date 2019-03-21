import sys
import os

import pygame
from pygame.sprite import *
from pygame.font import Font

from bullet import Bullet
from alien import Alien


file_path = os.path.dirname(__file__)
laser_path = os.path.join(file_path, 'audio', 'laser_blast.mp3')
explosion_path = os.path.join(file_path, 'audio', 'explosion.mp3')

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
        alien_group.update(settings)
        
        for alien in alien_group.copy():
                if alien.rect.x == -666 and alien.rect.y == -666:
                        alien_group.remove(alien)
                        if settings.lives <= 0:
                                return_val = True
                                return return_val

        #Remove dead aliens and player_bullets
        hit_bullet_group = Group()
        for alien in alien_group:
               hit_bullet_group.add(spritecollide(alien, bullet_group, True))
        for bullet in hit_bullet_group:
                pygame.mixer.music.load(explosion_path)
                pygame.mixer.music.play()
                settings.change_score(1)
                spritecollide(bullet, alien_group, True)

        #Update scoreboard
        update_scoreboard(screen, settings)        

        #Check death
        collide_list = spritecollide(ship, alien_group, False)
        return_val = False
        if collide_list:
                if settings.death_safety_counter == 200:
                        settings.lives -= 1
                        
                        path = os.path.join(file_path, 'audio', 'impact_alarm.mp3')
                        pygame.mixer.music.load(path)
                        pygame.mixer.music.play()

                        settings.death_safety_counter = 0

                        ship.rect.centerx = screen.get_rect().centerx
                        ship.rect.bottom = screen.get_rect().bottom
                        if settings.lives <= 0:
                                return_val = True
                else:
                        settings.death_safety_counter += 1

        #Redraw whole screen
        pygame.display.flip()

        return return_val

def remove_offscreen_bullets(bullet_group):
        """Remove bullets that exit the screen"""
        for bullet in bullet_group.copy():
                if bullet.rect.centery <= 0:
                        bullet_group.remove(bullet)

def update_scoreboard(screen, settings):
        """Updates and redraws scoreboard"""
        font = Font(None, 55)
        text = 'Score: {val}    Lives: {val2}'.format(val = settings.score, val2 = settings.lives)
        text_surface = font.render(text, True, (200, 200, 200), (40, 40, 40))
        
        text_rect = text_surface.get_rect()
        text_rect.x = 0
        text_rect.y = 0

        screen.blit(text_surface, text_rect)

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
                        pygame.mixer.music.load(laser_path)
                        bullet_group.add(Bullet(ship))
                        pygame.mixer.music.play()

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

def show_tutorial(screen):
        """Make visible the controls screen"""
        screen_rect = screen.get_rect()
        #Background color: light-grey
        

        #Load controls image
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'images', 'controls', 'arrow_keys_spacebar.png')
        image = pygame.image.load(path)
        image_rect = image.get_rect()

        #Create title splash
        font = Font(None, 72)
        text = 'alien invasion: a christopher wilson game'.title()
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()

        #Position surfaces
        text_rect.centerx = screen_rect.centerx
        text_rect.centery = 150

        image_rect.centerx = screen_rect.centerx
        image_rect.centery = 350

        #Loading screen
        loading_color = (45, 90, 200)
        loading_rect = Rect(screen_rect.left, screen_rect.bottom + 500, 1, 500)

        #Blit to screen
        while True:
                screen.fill((195, 195, 195))
                screen.blit(text_surface, text_rect)
                screen.blit(image, image_rect)
                pygame.draw.rect(screen, loading_color,  loading_rect)

                pygame.display.flip()

                loading_rect.width += 1

                if loading_rect.width >= 1200:
                        break

def game_over(screen, game_settings):

        screen_rect = screen.get_rect()
        screen.fill((213, 213, 213))
        
        #Create title splash
        title_font = Font(None, 72)
        title_text = 'game over'.upper()
        title_surface = title_font.render(title_text, True, (255, 15, 35))
        title_rect = title_surface.get_rect()

        #Create score splash
        score_font = Font(None, 60)
        score_text = 'Score: {scr}'.format(scr = game_settings.score)
        score_surface = title_font.render(score_text, True, (255, 15, 35))
        score_rect = score_surface.get_rect()

        #Position surfaces
        title_rect.centerx = screen_rect.centerx
        title_rect.centery = 150

        score_rect.centerx = screen_rect.centerx
        score_rect.centery = 250

        screen.blit(title_surface, title_rect)
        screen.blit(score_surface, score_rect)
        pygame.display.flip()
        pygame.time.wait(10000)
        return False