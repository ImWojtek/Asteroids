from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        # Remove the shot if it goes off-screen
        if (self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius or
            self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius):
            self.kill()