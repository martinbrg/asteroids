import pygame
from constants import *
from player import *

def main():
    pygame.init()
    #getting a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #the next 2 are for adjusting the FPS rate
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")

    #new player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)


    while True:
        #this will help actually quitting the infinite loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        #thats the refresh, for the sprites and afterwards for the entire screen:
        player.draw(screen, "white")
        pygame.display.flip()
        dt = clock.tick(1)/1000
        #elihw ...end of game loop





#calling main function, but not from another Python class
if __name__ == "__main__":
    main()

