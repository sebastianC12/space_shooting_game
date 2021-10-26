import pygame
from settings import Settings
from ships import Ships

class Bullets:
    def __init__(self, battle_ship):
        self.screen = battle_ship.screen
        self.settings = battle_ship.settings
        self.refreshes = 0
        self.ships = Ships(self)

        # Bullets color
        self.red_color = self.settings.red_bullet_color
        self.blue_color = self.settings.blue_bullet_color

        # Bullets Rect
        self.red_bullet_rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.blue_bullet_rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        # Bullets spawn
        self.red_bullet_rect.center = battle_ship.ships.red.midright
        self.blue_bullet_rect.center = battle_ship.ships.blue.midleft

        # Store bullets pos into a decimal
        self.red_bullet_rect_float = float(self.red_bullet_rect.x)
        self.blue_bullet_rect_float = float(self.blue_bullet_rect.x)

    def update_bullet(self, color):
        # Bullets movement
        if color == "red":
            self.red_bullet_rect_float += self.settings.bullet_speed / 3
            self.red_bullet_rect.x = self.red_bullet_rect_float

        elif color == "blue":
            self.blue_bullet_rect_float -= self.settings.bullet_speed / 3
            self.blue_bullet_rect.x = self.blue_bullet_rect_float

    def draw_bullet(self, color):
        # Update bullet on the screen
        if color == "red":
            pygame.draw.rect(self.screen, self.red_color, self.red_bullet_rect)
        elif color == "blue":
            pygame.draw.rect(self.screen, self.blue_color, self.blue_bullet_rect)


