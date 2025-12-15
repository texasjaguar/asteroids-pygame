import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280\nScreen height: 720")
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable,shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    afield = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        updatable.update(dt)
        player.shot_cd -= dt
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for obj in asteroids:
            for shot in shots:
                if obj.collides_with(shot):
                    log_event("asteroid_shot")
                    obj.split()
                    shot.kill()
        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
