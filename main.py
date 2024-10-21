import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    # Create the player object
    player_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0
    while True:
        # Check if the user has closed the game windows
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update Section
        for item in updatable:
            item.update(dt)
        
        
        for asteroid in asteroids:
            # Check if we're colliding with a bullet
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()
                    
            if asteroid.is_colliding(player_ship):
                print("Game Over")
                return
        #Drawing Section 
        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)
        
        # Refresh the screen
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()