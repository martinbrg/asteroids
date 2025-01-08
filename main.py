import pygame
from constants import *

def main():
    pygame.init()
    #getting a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    while True:
        #this will help actually quitting the infinite loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        #thats the refresh:
        pygame.display.flip()
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")





#calling main function, but not from another Python class
if __name__ == "__main__":
    main()

