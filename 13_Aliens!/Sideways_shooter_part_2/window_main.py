#Name: Aurelio Siordia
#Date: 12/04/23

import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien

#12-1 Blue Sky
class WindowMainGame: 
    """ """
    
    def __init__(self):
        """ """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()        
        self.ship = Ship(self)
        self._create_fleet()

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
        #if event.key == pygame.K_RIGHT:
        #    self.ship.moving_right = True
        #elif event.key == pygame.K_LEFT:
        #    self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True            
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Response to key releases."""
        #if event.key == pygame.K_RIGHT:
        #    self.ship.moving_right = False
        #elif event.key == pygame.K_LEFT:
        #    self.ship.moving_left = False
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
            self._fire_bullet()

    def _update_screen(self):        
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()        
        self.aliens.draw(self.screen)         
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
        self._check_bullet_alien_collisions()
 
    def _create_fleet(self):
        """Create the fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_width = self.ship.rect.width
        available_space_x = (self.settings.screen_width - (3 * alien_width)
                             - ship_width)
        number_aliens_x = available_space_x // ( 2 * alien_width)
        
        #Determine the number of rows of aliens that fit on the screen        
        available_space_y = (self.settings.screen_height -
                             3 * alien_height)
        number_rows = available_space_y // (2 * alien_height)
                
        #Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):                        
                self._create_alien(alien_number, row_number)
     
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = ((self.settings.screen_width - alien_width) -
                   (2 * alien_width * alien_number))
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number                         
        print(f"{alien.rect.x} {alien.rect.y}")
        self.aliens.add(alien)

    def  _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()        

    def _check_fleet_edges(self):
        """Responds appropiately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Check for any bullets tha have hit aliens.
        # If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()    

    def run_game(self):
        """ """
        while True:
            self._check_events()
            self._update_bullets()
            self.ship.update()
            self._update_aliens()
            self._update_screen()     


if __name__ == '__main__':
    wa_game = WindowMainGame()
    wa_game.run_game()

