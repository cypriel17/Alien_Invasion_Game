import unittest
import pygame
from alien import Alien
from alien_invasion import AlienInvasion
from settings import Settings

class TestAlien(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings = Settings()
        self.ai_game = AlienInvasion()  # Assuming AlienInvasion is properly instantiated
        self.ai_game.screen = self.screen
        self.ai_game.settings = self.settings

    def tearDown(self):
        pygame.quit()

    def test_alien_initialization(self):
        alien = Alien(self.ai_game)
        self.assertEqual(alien.rect.x, alien.rect.width)
        self.assertEqual(alien.rect.y, alien.rect.height)
        self.assertEqual(alien.x, float(alien.rect.x))

    def test_alien_update(self):
        alien = Alien(self.ai_game)
        initial_x = alien.rect.x
        alien.update()
        self.assertEqual(alien.rect.x, initial_x + (self.settings.alien_speed * self.settings.fleet_direction))

    def test_check_edges(self):
        alien = Alien(self.ai_game)
        # Move the alien to the edge
        alien.rect.x = 0
        self.assertTrue(alien.check_edges())

        # Move the alien back to the center of the screen
        alien.rect.x = self.settings.screen_width // 2
        self.assertFalse(alien.check_edges())


if __name__ == '__main__':
    unittest.main()
