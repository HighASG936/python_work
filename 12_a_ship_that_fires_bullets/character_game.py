
import pygame

class Character:
    """ """
    
    def __init__(self, wa_game):
        """ """
        self.screen = wa_game.screen
        self.screen_rect = wa_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
             

