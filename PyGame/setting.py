class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (51, 51, 153)

        # Ship settings.
        self.ship_speed_factor = 3

        # Bullet settings.
        self.bullet_speed_factor = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 91, 173, 66
        self.bullets_allowed = 3
