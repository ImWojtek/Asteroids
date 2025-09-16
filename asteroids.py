from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        # Wrap around screen edges
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius