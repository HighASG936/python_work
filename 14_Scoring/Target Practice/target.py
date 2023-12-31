"""

"""
import pygame
from pygame.sprite import Sprite

class Target:
    """ """
    
    def __init__(self, tp_game):
        """ """
        super().__init__()
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen.get_rect()
        self.settings = tp_game.settings
        self.color = self.settings.target_color
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
                                       self.settings.target_height)
        self.rect.midright = self.screen_rect.midright
        
        self.y = float(self.rect.y)

    def draw_target(self):
        """ """
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    def update(self):
        """ """
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y         
        
    def check_edges(self):
        """ """
        screen_rect = self.screen.get_rect()
        if (self.rect.bottom >= screen_rect.bottom or
            self.rect.top <= screen_rect.top ):
            return True
            
            