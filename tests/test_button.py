import unittest

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pygame
from main import AlienInvasion
from button import Button

class TestButton(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.ai_game = AlienInvasion()
        self.button = Button(self.ai_game, "Play")
        
    def test_initialization(self):
        """Test if button is initialized correctly"""
        expected_center = (600, 400)
        self.assertTrue(isinstance(self.button, Button))
        self.assertEqual(self.button.width, 200)
        self.assertEqual(self.button.height, 50)
        self.assertEqual(self.button.button_color, (0, 255, 0))
        self.assertEqual(self.button.text_color, (255, 255, 255))
        self.assertTrue(isinstance(self.button.font, pygame.font.Font))
        self.assertEqual(self.button.rect.center, expected_center)
        self.assertIsNotNone(self.button.msg_image)
        self.assertIsNotNone(self.button.msg_image_rect)

    def test_prep_msg(self):
        """Test if _prep_msg method prepares message correctly"""
        expected_center = (600, 400)
        self.button._prep_msg("Play")
        self.assertEqual(expected_center, self.button.rect.center)
        # Check if msg_image is correctly rendered

    
if __name__ == '__main__':
    unittest.main()