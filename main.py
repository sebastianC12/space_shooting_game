import pygame
import sys
from settings import Settings
from ships import Ships
from bullets import Bullets
from health import HealthBar
from end_screen import EndScreen
from particles import Particles


class BattleShip:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen_image = pygame.image.load("C:\\Users\\Sebi\\Desktop\\HkaoI.png")
        self.screen_image = pygame.transform.scale(self.screen_image, (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Battle Ship")
        self.ships = Ships(self)
        self.bullets = Bullets(self)
        self.health = HealthBar(self)
        self.end_screen = EndScreen(self)
        self.red_bullets = []
        self.blue_bullets = []

        self.pause = True

    def run_game(self):
        while True:
            if self.health.current_red_ship_health == 0 or self.health.current_blue_ship_health == 0:
                self._game_end_check()
                self.screen.blit(self.settings.image_play_button,
                                 (self.screen.get_width() / 5, self.screen.get_height() / 2))
                self.screen.blit(self.settings.image_quit_button,
                                 (self.screen.get_width() / 1.5, self.screen.get_height() / 2))
                pygame.display.update()
                self._check_events()
                self._check_events_while_paused()
                self.ships.ship_movement()
                self._remove_bullets()
            else:
                self._check_events()
                self.ships.ship_movement()
                self._remove_bullets()
                self._update_screen()

    def _check_events_while_paused(self):
        self.pos = pygame.mouse.get_pos()
        if self.settings.rect_play_button.collidepoint(self.pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.health.current_red_ship_health = 200
                self.health.current_blue_ship_health = 200
                self.ships.red.midleft = self.ships.screen_rect.midleft
                self.ships.blue.midright = self.ships.screen_rect.midright
                self.ships.ship_start_point()
                self.run_game()
        if self.settings.rect_quit_button.collidepoint(self.pos):
            if pygame.mouse.get_pressed()[0] == 1:
                sys.exit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

            # Shoot bullets
            elif event.key == pygame.K_SPACE and len(self.red_bullets) < self.settings.bullets_allowed:
                self.settings.laser_sound1.play()
                self._fire_red_bullet()
                print(self.red_bullets)
            elif event.key == pygame.K_RCTRL and len(self.blue_bullets) < self.settings.bullets_allowed:
                self.settings.laser_sound2.play()
                self._fire_blue_bullet()
                print(self.blue_bullets)
            # Red ship key down movement
            elif event.key == pygame.K_d:
                self.ships.red_moving_right = True
            elif event.key == pygame.K_a:
                self.ships.red_moving_left = True
            elif event.key == pygame.K_w:
                self.ships.red_moving_up = True
            elif event.key == pygame.K_s:
                self.ships.red_moving_down = True
            # Blue ship key down movement
            elif event.key == pygame.K_RIGHT:
                self.ships.blue_moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ships.blue_moving_left = True
            elif event.key == pygame.K_UP:
                self.ships.blue_moving_up = True
            elif event.key == pygame.K_DOWN:
                self.ships.blue_moving_down = True

    def _check_keyup_events(self, event):
        if event.type == pygame.KEYUP:
            # Red ship key up movement
            if event.key == pygame.K_d:
                self.ships.red_moving_right = False
            elif event.key == pygame.K_a:
                self.ships.red_moving_left = False
            elif event.key == pygame.K_w:
                self.ships.red_moving_up = False
            elif event.key == pygame.K_s:
                self.ships.red_moving_down = False
            # Blue ship key up movement
            elif event.key == pygame.K_RIGHT:
                self.ships.blue_moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ships.blue_moving_left = False
            elif event.key == pygame.K_UP:
                self.ships.blue_moving_up = False
            elif event.key == pygame.K_DOWN:
                self.ships.blue_moving_down = False

    def _fire_red_bullet(self):
        new_red_bullet = Bullets(self)
        self.red_bullets.append(new_red_bullet)

    def _fire_blue_bullet(self):
        new_blue_bullet = Bullets(self)
        self.blue_bullets.append(new_blue_bullet)

    def _remove_bullets(self):
        for bullet in self.red_bullets + self.blue_bullets:

            # Collision detection
            if self.ships.red.colliderect(bullet.blue_bullet_rect):
                self.settings.explosion.play()
                self.health_bar_update("red")
                self.blue_bullets.remove(bullet)
                self.health.current_red_ship_health -= 50
            elif self.ships.blue.colliderect(bullet.red_bullet_rect):
                self.settings.explosion.play()
                self.health_bar_update("blue")
                self.red_bullets.remove(bullet)
                self.health.current_blue_ship_health -= 50

            # Bullet out of bounds detection
            elif bullet.red_bullet_rect.left > 900:
                self.red_bullets.remove(bullet)
            elif bullet.blue_bullet_rect.right < 0:
                self.blue_bullets.remove(bullet)

    def health_bar_update(self, color):
        if color == "red":
            self.settings.red_ship_current_health -= 50
            print(self.settings.red_ship_current_health)
            print("Blue hit red ship")
        elif color == "blue":
            self.settings.blue_ship_current_health -= 50
            print(self.settings.blue_ship_current_health)
            print("Red hit blue ship")

    def _game_end_check(self):

        self.ships.red_moving_right = False
        self.ships.red_moving_left = False
        self.ships.red_moving_up = False
        self.ships.red_moving_down = False

        self.ships.blue_moving_right = False
        self.ships.blue_moving_left = False
        self.ships.blue_moving_up = False
        self.ships.blue_moving_down = False

        for bullet in self.red_bullets:
            self.red_bullets.pop()
        for bullet in self.blue_bullets:
            self.blue_bullets.pop()


    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.screen.blit(self.screen_image, (0, 0))
        self.screen.blit(self.ships.red_ship, (self.ships.red.x, self.ships.red.y))
        self.screen.blit(self.ships.blue_ship, (self.ships.blue.x, self.ships.blue.y))
        self.screen.blit(self.health.hbar_red_surface, (125, 10)) # Red health bar for red ship
        self.screen.blit(self.health.decrease_health("red"), (125, 10)) # Green health bar for red ship
        self.screen.blit(self.health.hbar_blue_surface, (575, 10)) # Red health bar for blue ship
        self.screen.blit(self.health.decrease_health("blue"),(575, 10)) # Green health bar for blue ship

        if self.health.current_red_ship_health == 0:
            self.screen.blit(self.health.textsurface_blue_ship_won, (self.screen.get_width() / 2 - self.health.textsurface_blue_ship_won.get_width() / 2, self.screen.get_height() / 3 - self.health.textsurface_blue_ship_won.get_height() / 2))
            self.pause = True
        elif self.health.current_blue_ship_health == 0:
            self.screen.blit(self.health.textsurface_red_ship_won, (self.screen.get_width() / 2 - self.health.textsurface_blue_ship_won.get_width() / 2, self.screen.get_height() / 3 - self.health.textsurface_blue_ship_won.get_height() / 2))
            self.pause = True

        for bullet in self.red_bullets:
            bullet.update_bullet("red")
            bullet.draw_bullet("red")
        for bullet in self.blue_bullets:
            bullet.update_bullet("blue")
            bullet.draw_bullet("blue")

        pygame.display.flip()

if __name__ == "__main__":
    battle_ship = BattleShip()
    battle_ship.run_game()

