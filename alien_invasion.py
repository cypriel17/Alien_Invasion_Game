import sys

import pygame

class AlienInvasion:
    """Overall class t manage the game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources"""

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Wars")

    def run_game(self):
        """start the main loop of the game"""

        while True:
            #listen to keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0);


            #make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    #make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

