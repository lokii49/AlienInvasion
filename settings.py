import pygame


class Settings:
    """A class store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static setting"""
        # Screen Settings
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.bg_image = pygame.image.load('images/sky-bg.bmp')
        self.random_image = pygame.image.load('images/star.bmp')

        # Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        # How quickly values alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughtout the game."""
        self.ship_speed = 1.5
        self.ship_limit = 3
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increased speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)