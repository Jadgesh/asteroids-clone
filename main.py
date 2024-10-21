import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    # Create the player object
    player_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    while True:
        # Check if the user has closed the game windows
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update Section
        player_ship.update(dt)
        #Drawing Section 
        screen.fill("black")
        
        player_ship.draw(screen)
        # Refresh the screen
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()