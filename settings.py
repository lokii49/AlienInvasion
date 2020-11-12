import pygame


class Settings:
    """A class store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's setting"""
        # Screen Settings
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.bg_image = pygame.image.load('images/sky-bg.bmp')

        # Ship settings
        self.ship_speed = 1.5

        #bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 5
