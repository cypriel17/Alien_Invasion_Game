import unittest
from settings import Settings

class TestSettings(unittest.TestCase):

    def setUp(self):
        self.settings = Settings()

    def test_init(self):
        self.assertEqual(self.settings.screen_width, 1200)
        self.assertEqual(self.settings.screen_height, 800)
        self.assertEqual(self.settings.bg_color, (255, 255, 255))
        self.assertAlmostEqual(self.settings.ship_speed, 1.5)
        self.assertEqual(self.settings.bullets_allowed, 3)
        self.assertEqual(self.settings.alien_speed, 1)
        self.assertEqual(self.settings.fleet_drop_speed, 10)

if __name__ == '__main__':
    unittest.main()
