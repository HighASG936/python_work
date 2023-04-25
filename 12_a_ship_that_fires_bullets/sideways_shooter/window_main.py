#Name: Aurelio Siordia
#Date: 12/04/23

import sys
import pygame
from character_game import Character
from settings import Settings
from bullet import Bullet

#12-1 Blue Sky
class WindowMainGame: 
    """ """
    
    def __init__(self):
        """ """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.character_game = Character(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start tha main loop for the game"""
        while True:
            self._check_events()
            self.character_game.update()
            self._update_bullets()                                                            
            self._update_screen()            

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

  
    def _check_keydown_events(self, event):
        """Respond to keypress."""
        if event.key == pygame.K_RIGHT:
            self.character_game.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.character_game.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_UP:
            self.character_game.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.character_game.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Response to key releases."""
        if event.key == pygame.K_RIGHT:
            self.character_game.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.character_game.moving_left = False
        elif event.key == pygame.K_UP:
            self.character_game.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.character_game.moving_down = False              
  
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
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        #print(len(self.bullets))        
        
  
    def _update_screen(self):        
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.character_game.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    wa_game = WindowMainGame()
    wa_game.run_game()

