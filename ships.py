import pygame
import os

class Ships:
    def __init__(self, battle_ship):
        self.screen = battle_ship.screen
        self.settings = battle_ship.settings
        self.screen_rect = battle_ship.screen.get_rect()

        # Load ships image
        dirname = os.path.dirname(__file__)
        self.image_blue_ship = pygame.image.load(os.path.join(dirname, "images/blue_ship.bmp"))
        self.image_red_ship = pygame.image.load(os.path.join(dirname, "images/red_ship.bmp"))

        # Rotated ships | red ship left, blue ship right
        self.red_ship = pygame.transform.rotate(self.image_red_ship, 270)
        self.blue_ship = pygame.transform.rotate(self.image_blue_ship, 90)

        # Ships weight and height
        self.ship_width = self.image_blue_ship.get_width()
        self.ship_height = self.image_blue_ship.get_height()

        # Ships rectangle position
        self.red = self.image_red_ship.get_rect()
        self.blue = self.image_blue_ship.get_rect()

        # Start each ship in middle left and right
        self.red.midleft = self.screen_rect.midleft
        self.blue.midright = self.screen_rect.midright


        # Ships movement flags
        self.red_moving_right = False
        self.red_moving_left = False
        self.red_moving_up = False
        self.red_moving_down = False

        self.blue_moving_right = False
        self.blue_moving_left = False
        self.blue_moving_up = False
        self.blue_moving_down = False

        # Store ships pos into a decimal
        self.red_float_x = float(self.red.x)
        self.red_float_y = float(self.red.y)

        self.blue_float_x = float(self.blue.x)
        self.blue_float_y = float(self.blue.y)

    def ship_start_point(self):
        self.red.midleft = self.screen_rect.midleft
        self.blue.midright = self.screen_rect.midright
        self.red_float_x = float(self.red.x)
        self.red_float_y = float(self.red.y)

        self.blue_float_x = float(self.blue.x)
        self.blue_float_y = float(self.blue.y)

    def ship_movement(self):
        if self.red_moving_right and self.red.x < self.screen_rect.right - self.ship_width + 8:
            self.red_float_x += self.settings.ship_speed
            self.red.x = self.red_float_x
        if self.red_moving_left and self.red.x > 0:
            self.red_float_x -= self.settings.ship_speed
            self.red.x = self.red_float_x
        if self.red_moving_up and self.red.y > 0 + self.ship_height:
            self.red_float_y -= self.settings.ship_speed
            self.red.y = self.red_float_y
        if self.red_moving_down and self.red.y < self.screen_rect.bottom - self.ship_height * 2 + 30:
            self.red_float_y += self.settings.ship_speed
            self.red.y = self.red_float_y

        if self.blue_moving_right and self.blue.x < self.screen_rect.right - self.ship_width + 8:
            self.blue_float_x += self.settings.ship_speed
            self.blue.x = self.blue_float_x
        if self.blue_moving_left and self.blue.x > self.screen_rect.left:
            self.blue_float_x -= self.settings.ship_speed
            self.blue.x = self.blue_float_x
        if self.blue_moving_up and self.blue.y > 0 + self.ship_height:
            self.blue_float_y -= self.settings.ship_speed
            self.blue.y = self.blue_float_y
        if self.blue_moving_down and self.blue.y < self.screen_rect.bottom - self.ship_height * 2 + 30:
            self.blue_float_y += self.settings.ship_speed
            self.blue.y = self.blue_float_y



