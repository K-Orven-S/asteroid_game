import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity, radius):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (round(self.position.x), round(self.position.y)), SHOT_RADIUS, width=2)

    def update(self, dt):
        self.position += self.velocity * dt      