import pygame
import unittest

from alien_invasion import AlienInvasion
from settings import Settings
from alien import Alien

class TestAlien(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings = Settings()
        self.ai_game = AlienInvasion()
        self.alien = Alien(self.ai_game)
        
    def test_initialization(self):
        """Test initialized correctly"""
        self.assertTrue(isinstance(self.alien, Alien))
        self.assertEqual(self.alien.rect.x, self.alien.rect.width)
        self.assertEqual(self.alien.rect.y, self.alien.rect.height)
        self.assertTrue(isinstance(self.alien.x, float))
    
    def test_alien_position(self):
        """Test for corrrect positioning"""
        pos_x = self.alien.x
        alien_pos_speed = self.settings.alien_speed * self.settings.fleet_direction
        self.alien.update()
        self.assertAlmostEqual(self.alien.x, pos_x + (alien_pos_speed), places=7)
        
    def test_check_edges(self):
        """Test for checking the fleet has reached the edge or not"""
        self.alien.rect.right = self.screen.get_rect().right
        self.assertTrue(self.alien.check_edges())

        self.alien.rect.left = 0
        self.assertTrue(self.alien.check_edges())

        # Alien not at edge
        self.alien.rect.right = 50
        self.alien.rect.left = 50
        self.assertFalse(self.alien.check_edges())

        
if __name__ == '__main__':
    unittest.main()