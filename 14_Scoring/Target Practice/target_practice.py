#Name: Aurelio Siordia
#Date: 12/04/23

import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from time import sleep
from game_stats import GameStats
from button import Button
from target import Target

#12-1 Blue Sky
class TargetPractice: 
    """ """
    
    def __init__(self):
        """ """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Target Practice")
        
        #Create an instance to store game statistics
        self.stats = GameStats(self)
        
        self.bullets = pygame.sprite.Group()     
        self.ship = Ship(self)
        
        #Make the Play button.
        self.play_button = Button(self, "Play")
        
        self.target = Target(self)
        
        self.get_shoot = False #check if you've shoot anytime

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)                

    def _check_play_button(self, mouse_pos):
        """Start new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True         

    def _check_keydown_events(self, event):
        """Respond to keypress."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True            
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_q:
            sys.exit()            

    def _check_keyup_events(self, event):
        """Response to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_q:
            sys.exit()            

    def _check_keyup_events(self, event):
        """Response to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_SPACE:
            self.get_shoot = True 
            self._fire_bullet()

    def _update_screen(self):        
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()               
        self.target.draw_target()
        
        #Draw the play button if the game is inactive
        if not self.stats.game_active:            
            self.play_button.draw_button()
        
        pygame.display.flip()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:            
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()
            
        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            #Decrement ships_left.
            self.stats.ships_left -= 1
        
            #Get rid of any remaining aliens and bullets
            self.bullets.empty()
        
            #Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
        
            #Pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_target(self):
        """ """
        self._check_target_edges()
        self.target.update()        
        self.target.draw_target()
        
        if self.get_shoot:            
            if not pygame.sprite.spritecollideany(self.target,self.bullets):
                if len(self.bullets) == 0:
                    self.settings.bullets_left -= 1
                    #print(self.settings.bullets_left)
                    self.get_shoot = False
            else:
                #print("Asserted")
                self.get_shoot = False
                
        if self.settings.bullets_left <= 0:
            self.stats.game_active = False
            self.stats.reset_stats()            
                   
        
    
    
    def _check_target_edges(self):
        """ """
        if self.target.check_edges():
            self._change_target_direction()
    
    def _change_target_direction(self):
        """ """
        self.settings.target_direction *= -1        

    def run_game(self):
        """Start tha main loop for the game"""        
        while True:
            self._check_events()
            
            if self.stats.game_active:    
                self.ship.update()
                self._update_bullets()
                self._update_target()
            
            self._update_screen()         

if __name__ == '__main__':
    tp_game = TargetPractice()
    tp_game.run_game()

