import pygame
from pygame.sprite import Sprite

class Droprain(Sprite):
    """ """
    
    def __init__(self, rain_game):
        """ """
        super().__init__()
        self.screen = rain_game.screen
        self.settings = rain_game.settings

        # 
        self.image = pygame.image.load('images/droprain.bmp')
        self.rect = self.image.get_rect()
        
        # 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 
        self.y = float(self.rect.y)
        
        self.rain_freq = 10000

    def update(self):
        """ """
        self.y += self.settings.droprain_speed
        self.rect.y = self.y
    
    def is_down(self):
        if self.y >= self.settings.screen_height:
            return True
        else:
            return False
        
        
        
        
        