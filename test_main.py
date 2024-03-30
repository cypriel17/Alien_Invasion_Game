import unittest
from httpx import patch
import pygame
from alien_invasion import AlienInvasion
from settings import Settings

class TestAlienInvasion(unittest.TestCase):

    def setUp(self):
        self.settings = Settings()
        self.ai = AlienInvasion()
        pygame.display.init()
        pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def test_init(self):
        self.assertIsInstance(self.ai.screen, pygame.Surface)
        self.assertEqual(self.ai.screen.get_size(), (self.settings.screen_width, self.settings.screen_height))
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

    def test_event_handling(self):
        # Simulate keyboard events
        key_down_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
        key_up_event = pygame.event.Event(pygame.KEYUP, key=pygame.K_RIGHT)
        
        # Send keyboard events
        pygame.event.post(key_down_event)
        self.ai._check_events()
        self.assertTrue(self.ai.ship.moving_right)  # Check if moving_right is set to True
        
        pygame.event.post(key_up_event)
        self.ai._check_events()
        self.assertFalse(self.ai.ship.moving_right)

    def test_fullscreen_mode(self):
        self.assertTrue(pygame.FULLSCREEN)
        self.assertEqual(self.ai.settings.screen_width, self.ai.screen.get_rect().width)
        self.assertEqual(self.ai.settings.screen_height, self.ai.screen.get_rect().height)

    def test_quit_game_with_q(self):
        with self.assertRaises(SystemExit):
            self.ai._check_keydown_events(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_q))

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()