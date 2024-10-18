import pygame
from constants import *

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Check if the user has closed the game windows
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Filling the screen with black
        screen.fill((0,0,0))
        
        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()