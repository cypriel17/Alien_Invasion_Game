import unittest

import pygame
from alien_invasion import AlienInvasion
from game_stats import GameStats

class TestGameStats(unittest.TestCase):
    def setUp(self):
        
        self.screen = pygame.display.set_mode((1200, 800))
        self.ai_game = AlienInvasion()
        self.stats = GameStats(self.ai_game)

    def test_initialization(self):
        self.assertEqual(self.stats.game_active, False)
        self.assertEqual(self.stats.ships_left, self.stats.settings.ship_limit)
        self.assertEqual(self.stats.score, 0)
        self.assertEqual(self.stats.level, 1)

    def test_reset_stats(self):
        self.stats.game_active = True
        self.stats.ships_left = 2
        self.stats.score = 100
        self.stats.level = 3

        self.stats.reset_stats()

        self.assertEqual(self.stats.game_active, True)
        self.assertEqual(self.stats.ships_left, self.stats.settings.ship_limit)
        self.assertEqual(self.stats.score, 0)
        self.assertEqual(self.stats.level, 1)

    def test_save_high_score(self):
        self.stats.score = 200
        self.stats.high_score = 150

        # Read the high score from a file
        filename = 'high_score.txt'
        try:
            with open(filename, 'r') as file:
                high_score = int(file.read())
        except FileNotFoundError:
            high_score = 0

        # Update the high score if the current score is higher
        if self.stats.score > high_score:
            high_score = self.stats.score

        # Save the updated high score to the file
        with open(filename, 'w') as file:
            file.write(str(high_score))

        self.stats.high_score = high_score

        self.assertEqual(self.stats.high_score, 200)


if __name__ == '__main__':
    unittest.main()
