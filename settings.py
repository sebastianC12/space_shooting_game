import pygame
import os

class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 900
        self.screen_height = 500
        self.background_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 2.5
        self.red_ship_current_health = 200
        self.blue_ship_current_health = 200


        # Bullet settings
        self.bullet_speed = 8
        self.bullet_width = 15
        self.bullet_height = 3
        self.red_bullet_color = (255, 0, 0)
        self.blue_bullet_color = (0, 0, 255)
        self.bullets_allowed = 3

        # Buttons
        dirname = os.path.dirname(__file__)
        self.image_play_button = pygame.image.load(os.path.join(dirname, "images/play_button.bmp"))
        self.image_play_button = pygame.transform.scale(self.image_play_button, (150, 110))
        self.image_quit_button = pygame.image.load(os.path.join(dirname, "images/quit_button.bmp"))
        self.image_quit_button = pygame.transform.scale(self.image_quit_button, (150, 110))

        # Get buttons rect
        self.rect_play_button = self.image_play_button.get_rect()
        self.rect_quit_button = self.image_quit_button.get_rect()

        self.rect_play_button.topleft = (900 / 5, 500 / 2)
        self.rect_quit_button.topleft = (900 / 1.5, 500 / 2)

        # Music / Sounds
        dirname = os.path.dirname(__file__)
        self.music = pygame.mixer.music.load(os.path.join(dirname, "sounds/backgrounds_music.ogg"))
        self.laser_sound1 = pygame.mixer.Sound(os.path.join(dirname, "sounds/pew_red_ship.ogg"))
        self.laser_sound2 = pygame.mixer.Sound(os.path.join(dirname, "sounds/pew_blue_ship.ogg"))
        self.explosion = pygame.mixer.Sound(os.path.join(dirname, "sounds/explosion.ogg"))
        pygame.mixer.music.play(-1)

