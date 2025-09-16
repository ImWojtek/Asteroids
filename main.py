# this allows us to use code from
# the open-source pygame library
# throughout this file
from shot import Shot
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill((0, 0, 0))  # Fill the screen with black
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                raise SystemExit(0)
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Amount of seconds between each loop


if __name__ == "__main__":
    main()
