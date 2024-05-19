import unittest

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pygame
from main import AlienInvasion
from settings import Settings


class TestShip(unittest.TestCase):

    def setUp(self):
        self.settings = Settings()
        pygame.init()
        self.ai = AlienInvasion()
        pygame.display.init()
        pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  

    def test_init(self):
        ship = self.ai.ship
        self.assertIsInstance(ship.screen, pygame.Surface)
        self.assertIsInstance(ship.settings, Settings)
        self.assertIsInstance(ship.screen_rect, pygame.Rect)
        self.assertIsInstance(ship.image, pygame.Surface)
        self.assertIsInstance(ship.rect, pygame.Rect)
        self.assertEqual(ship.rect.midbottom, ship.screen_rect.midbottom)
        self.assertEqual(ship.x, float(ship.rect.x))
        self.assertFalse(ship.moving_right)
        self.assertFalse(ship.moving_left)

    def test_update_movement(self):
        ship = self.ai.ship
        settings = ship.settings

        # Simulate movement to the right
        ship.moving_right = True
        initial_x = ship.x
        ship.update()
        self.assertAlmostEqual(ship.x, initial_x + settings.ship_speed)

        # Simulate movement to the left
        ship.moving_right = False
        ship.moving_left = True
        initial_x = ship.x
        ship.update()
        self.assertAlmostEqual(ship.x, initial_x - settings.ship_speed)

    def test_blitme(self):
        ship = self.ai.ship
        # screen = ship.screen
        initial_rect = ship.rect.copy()

        # Blit the ship
        ship.blitme()

        # Check if the ship is correctly blitted to the screen
        # self.assertTrue(screen.get_rect().colliderect(ship.rect))
        self.assertEqual(initial_rect, ship.rect)  # Ensure ship's rect hasn't changed after blitting

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
