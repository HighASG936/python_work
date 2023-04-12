#Name: Aurelio Siordia
#Date: 12/04/23

import sys
import pygame
from character_game import Character

#12-1 Blue Sky
class WindowMainGame: 
    """ """
    
    def __init__(self):
        """ """
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.character = Character(self)

    def run_game(self):
        """ """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((10,73,123))
            self.character.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    wa_game = WindowMainGame()
    wa_game.run_game()

