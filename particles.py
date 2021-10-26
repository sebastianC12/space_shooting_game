import pygame
import random


class Particles:
    def __init__(self, battle_ship):
        self.particles = []
        self.screen = battle_ship.screen

    def _create_particles(self):
        self.particles.append([[250, 250], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])
        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            pygame.draw.circle(self.screen, (255, 255, 255), particle[0], int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)
