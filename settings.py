from ship import Ship


class Settings:

    def __init__(self):
        """Intialize game's settings."""

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        #ship settings
        self.ship_speed = 1.5