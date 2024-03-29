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
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage the game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        #Initialize the ship
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop of the game"""

        while True:
            # Listen to keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # Redraw the screen during each pass through loop
            self.screen.fill(self.settings.bg_color) 
            self.ship.blitme()       

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
