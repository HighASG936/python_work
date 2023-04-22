"""


"""
import pygame
from droprain import Droprain
from settings import Settings
from random import randint
import sys

class Rain:
    """ """
    
    def __init__(self):
        """ """
        pygame.init()
        self.settings = Settings()
        self.counter = 0
        self.screen = pygame.display.set_mode(
             (self.settings.screen_width,
               self.settings.screen_height
             ))       
        pygame.display.set_caption("Rain")
        self.droprains_group = pygame.sprite.Group()
        self.raining()
    
    def raining(self):
        """ """
        droprain = Droprain(self)
        droprain_width, droprain_height = droprain.rect.size
        available_space_x = self.settings.screen_width #- (2 * droprain_width)
        number_droprains_x = available_space_x  // ( 6 * droprain_width)
        
        available_space_y = self.settings.screen_height -0 * droprain_height
        number_rows = available_space_y // (20 * droprain_height)
        for droprain_number in range(number_droprains_x):
            self._create_droprain(0, droprain_number)
    
    def _create_droprain(self, row_number, droprain_number):
        """ """
        droprain = Droprain(self)
        droprain_width, droprain_height = droprain.rect.size
        droprain.x = droprain_width * 6 * droprain_number
        droprain.rect.x = droprain.x * randint(0, 11)
        droprain.rect.y = droprain_height
        self.droprains_group.add(droprain)
        
    def _update_droprains(self):
        """ """                                           
        for single_droprain in self.droprains_group.copy():                                                
            if single_droprain.is_down():
                self.droprains_group.remove(single_droprain)
        
            if (self.counter > single_droprain.rain_freq and
                len(self.droprains_group) < 100 ):            
                self.counter = 0                
                self.raining()
            else:
                self.counter += 1
            #print(self.counter)
        
        self.droprains_group.update()

    def _update_screen(self):        
        """ """
        self.screen.fill(self.settings.bg_color)
        self.droprains_group.draw(self.screen)
        pygame.display.flip()

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                 self._check_keydown_events(event)    
 
    def _check_keydown_events(self, event):
        """Respond to keypress."""
        if event.key == pygame.K_q:
            sys.exit()


    def run_game(self):
        """ """        
        while True:
            self._check_events()
            self._update_droprains()
            self._update_screen() 
        
if __name__ == '__main__':
    #Make a game instance, and run the game
    rain = Rain()
    rain.run_game()
    
    