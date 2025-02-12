from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

import pygame

def main():

    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    
    print("Starting asteroids!")    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                pygame.quit()
                return

            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = (game_clock.tick(60))/1000


if __name__== "__main__":
    main()
    pygame.quit()
