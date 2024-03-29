"""
In Alien Invasion, the player controls a rocket ship that appears
at the bottom center of the screen. The player can move the ship
right and left using the arrow keys and shoot bullets using the
spacebar. When the game begins, a fleet of aliens fills the sky
and moves across and down the screen. The player shoots and
destroys the aliens. If the player shoots all the aliens, a new fleet
appears that moves faster than the previous fleet. If any alien hits
the player’s ship or reaches the bottom of the screen, the player
loses a ship. If the player loses three ships, the game ends.

"""


import sys

import pygame

class AlienInvasion:
    """Overall class t manage the game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources"""

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

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

