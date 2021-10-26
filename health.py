import pygame
from settings import Settings
from end_screen import EndScreen

class HealthBar:
    def __init__(self, battle_ship):
        self.screen = battle_ship.screen
        self.settings = battle_ship.settings
        self.screen_rect = battle_ship.screen.get_rect()
        # self.end_screen = EndScreen(self)

        self.color_red = (255, 0, 0)
        self.color_green = (0, 255, 0)
        self.color_blue = (0,0,255)


        # Red ship empty health bar
        self.hbar_red_surface = pygame.Surface((200, 20))
        self.hbar_red_surface.fill(self.color_red)

        # Blue ship red health bar
        self.hbar_blue_surface = pygame.Surface((200, 20))
        self.hbar_blue_surface.fill(self.color_red)

        # Red ship green health bar
        self.hbar_full_red_surface = pygame.Surface((200, 20))
        self.hbar_full_red_surface.fill(self.color_green)

        #Red ship rect
        self.hbar_full_red_surface_rect = pygame.Rect(125, 10, 200, 20)

        # Blue ship green health bar
        self.hbar_full_blue_surface = pygame.Surface((200, 20))
        self.hbar_full_blue_surface.fill(self.color_green)

        # Blue ship won message
        self.myfont = pygame.font.SysFont("Comic Sans MS", 50)
        self.textsurface_blue_ship_won = self.myfont.render("BLUE SHIP WON", False, self.color_blue)

        # Red ship won message
        self.myfont = pygame.font.SysFont("Comic Sans MS", 50)
        self.textsurface_red_ship_won = self.myfont.render("RED SHIP WON", False, self.color_red)

    current_red_ship_health = 200
    current_blue_ship_health = 200

    def decrease_health(self, color):

        if color == "red":
                self.hbar_full_red_surface = pygame.Surface((self.current_red_ship_health, 20))
                self.hbar_full_red_surface.fill(self.color_green)
                return self.hbar_full_red_surface
        elif color == "blue":
            self.hbar_full_blue_surface = pygame.Surface((self.current_blue_ship_health, 20))
            self.hbar_full_blue_surface.fill(self.color_green)
            return self.hbar_full_blue_surface
