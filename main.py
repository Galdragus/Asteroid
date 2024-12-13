import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock() 
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_sprites = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_sprites, updatable, drawable)
    AsteroidField.containers = ((updatable))
    Shot.containers = (updatable,drawable, player_shots)
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatables in updatable:
            updatables.update(dt)
        for rock in asteroid_sprites:
            if rock.check_collision( player):
                print("Game over!")
                raise SystemExit
            pass
        for rock in asteroid_sprites:
            for shot in player_shots:
                if shot.check_collision(rock):
                    shot.kill()
                    rock.split()
        Screen.fill((0,0,0))
        
        for drawables in drawable:
            drawables.draw(Screen)
        pygame.display.flip()
        dt = (time_clock.tick(60)/1000)
if __name__ == "__main__":

        main()
