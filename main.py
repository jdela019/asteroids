import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroid_group)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, player_shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        for sprite in updatable:
            sprite.update(dt)
        
        for obj in asteroid_group:
            if obj.collision(player):
                print("GAME OVER")
                sys.exit()
            for shot in player_shots:
                if shot.collision(obj):
                    shot.kill()
                    obj.split()

        screen.fill("black")

        shots_to_remove = []

        for obj in player_shots:
            obj.update(dt)
            if (obj.position.x < 0 or obj.position.x > SCREEN_WIDTH or obj.position.y < 0 or obj.position.y > SCREEN_HEIGHT):
              shots_to_remove.append(obj)
            obj.draw(screen)
        
        for obj in shots_to_remove:
            player_shots.remove(obj)


        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()


if __name__ == "__main__":
    main()