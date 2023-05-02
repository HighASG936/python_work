
import pygame

class Ship:
    """ """
    
    def __init__(self, wa_game):
        """Initialize the ship and set its starting position."""
        self.screen = wa_game.screen
        self.screen_rect = wa_game.screen.get_rect()
        self.settings = wa_game.settings
        
        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #Start each new ship at the left center of the screen.
        self.rect.left = self.screen_rect.left
        
        #Store a decimal value for the ship's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        #Movement flags
        self.moving_up = False
        self.moving_down = False
        
        self.increase = 1.1
        self.asserts = 0
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            
            
        #Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
             

