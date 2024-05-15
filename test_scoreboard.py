import pygame
import unittest
from alien_invasion import AlienInvasion
from scoreboard import Scoreboard
from settings import Settings
from game_stats import GameStats

class TestScoreboard(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings = Settings()
        self.ai_game = AlienInvasion()
        self.stats = GameStats(self.ai_game)
        self.scoreboard = Scoreboard(self.ai_game)

    def test_prep_score(self):
        """Test if score is properly prepared"""
        self.scoreboard.stats.score = 12345
        self.scoreboard.prep_score()
        self.assertEqual(self.scoreboard.score_image.get_rect().right, 1180)
        self.assertEqual(self.scoreboard.score_image.get_rect().top, 20)

    def test_prep_high_score(self):
        """Test if high score is properly prepared"""
        self.scoreboard.stats.high_score = 9999
        self.scoreboard.prep_high_score()
        self.assertEqual(self.scoreboard.high_score_image.get_rect().centerx, 600)
        self.assertEqual(self.scoreboard.high_score_image.get_rect().top, 20)

    def test_prep_level(self):
        """Test if level is properly prepared"""
        self.scoreboard.stats.level = 3
        self.scoreboard.prep_level()
        self.assertEqual(self.scoreboard.level_image.get_rect().right, 1180)
        self.assertEqual(self.scoreboard.level_image.get_rect().top, 88)  # Assuming 48 pixels between score and level

if __name__ == '__main__':
    unittest.main()
