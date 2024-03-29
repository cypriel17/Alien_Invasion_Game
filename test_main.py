import unittest
from httpx import patch
import pygame
from alien_invasion import AlienInvasion

class TestAlienInvasion(unittest.TestCase):

    def setUp(self):
        self.ai = AlienInvasion()
        pygame.display.init()
        pygame.display.set_mode((1200, 800))

    def test_init(self):
        self.assertIsInstance(self.ai.screen, pygame.Surface)
        self.assertEqual(self.ai.screen.get_size(), (1200, 800))
        self.assertEqual(pygame.display.get_caption()[0], 'Alien Invasion')

    def test_run_game(self):
        # Simulate QUIT event
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        with self.assertRaises(SystemExit) as cm:
            self.ai.run_game()
        
        self.assertEqual(cm.exception.code, 0)  # Check the exit code

    def test_run_game_quit_event(self):
        # Simulate QUIT event
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        with self.assertRaises(SystemExit) as cm:
            self.ai.run_game()
        
        self.assertEqual(cm.exception.code, 0)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
