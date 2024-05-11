from ship import Ship


class Settings:

    def __init__(self):
        """Intialize game's settings."""

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        #ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        self.initiliaze_dynamic_settings()
        
    def initiliaze_dynamic_settings(self):
        """Initialize the settings throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # right rep by 1; left rep by -1
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Incrrease speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale