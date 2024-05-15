import unittest

import pygame
from alien_invasion import AlienInvasion
from bullet import Bullet
from settings import Settings

class TestBullet(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings = Settings()
        self.ai_game = AlienInvasion()
        self.bullet = Bullet(self.ai_game)
        
    def test_initialization(self):
        """Test if bullet is initialized correctly"""
        self.assertTrue(isinstance(self.bullet, Bullet))
        self.assertEqual(self.bullet.rect.midtop, self.ai_game.ship.rect.midtop)
        self.assertEqual(self.bullet.color, self.settings.bullet_color)
        self.assertTrue(isinstance(self.bullet.y, float))

    def test_update(self):
        """Test if bullet updates its position correctly"""
        shot_y = self.bullet.y
        bullet_speed_y = shot_y - self.settings.bullet_speed
        self.bullet.update()
        self.assertAlmostEqual(self.bullet.y, bullet_speed_y, places=7)

    def test_draw_bullet(self):
        """Test if draw_bullet method correctly draws bullet to screen"""
        self.assertIsNone(self.bullet.draw_bullet())
    
if __name__ == '__main__':
    unittest.main()