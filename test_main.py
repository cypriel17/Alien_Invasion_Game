import unittest
from unittest.mock import patch
from io import StringIO
import sys
import pygame

from alien_invasion import AlienInvasion

class TestAlienInvasion(unittest.TestCase):

    def setUp(self):
        self.ai = AlienInvasion()

    def test_init(self):
        self.assertIsInstance(self.ai.screen, pygame.Surface)
        self.assertEqual(self.ai.screen.get_size(), (1200, 800))
        self.assertEqual(pygame.display.get_caption(), "Alien Invasion")

    @patch('sys.exit')
    def test_run_game(self, mock_exit):
        with patch('builtins.input', side_effect=[pygame.event.Event(pygame.QUIT)]):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.ai.run_game()
                self.assertTrue(mock_exit.called)
                self.assertEqual(mock_exit.call_args[0][0], 0)
                self.assertIn('pygame.quit()', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
