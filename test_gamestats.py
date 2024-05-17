# import unittest
# from game_stats import GameStats
# from settings import Settings

# class TestGameStats(unittest.TestCase):

#     def setUp(self):
#         self.settings = Settings()
#         self.stats = GameStats(self.settings)

#     def test_initialization(self):
#         """Test if GameStats is initialized correctly"""
#         self.assertTrue(isinstance(self.stats, GameStats))
#         self.assertFalse(self.stats.game_active)
#         self.assertEqual(self.stats.ships_left, self.settings.ship_limit)
#         self.assertEqual(self.stats.score, 0)
#         self.assertEqual(self.stats.high_score, 0)
#         self.assertEqual(self.stats.level, 1)

#     def test_reset_stats(self):
#         """Test if reset_stats method resets statistics correctly"""
#         self.stats.ships_left = 3
#         self.stats.score = 100
#         self.stats.high_score = 200
#         self.stats.level = 3

#         self.stats.reset_stats()

#         self.assertEqual(self.stats.ships_left, self.settings.ship_limit)
#         self.assertEqual(self.stats.score, 0)
#         self.assertEqual(self.stats.high_score, 200) 
#         self.assertEqual(self.stats.level, 1)

# if __name__ == '__main__':
#     unittest.main()

pass #for now