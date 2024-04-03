import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to present a single alien in fleet."""
    
    def __init__(self, ai_game):
        """Initialize the alien and set a starting position"""
    
        super().__init__()
        self.screen = ai_game.screen
        
        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/enemy_ship_1.jpeg')
        self.rect = self.image.get_rect()
        
        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # store the alien's exact horizontal position
        self.x = float(self.rect.x)