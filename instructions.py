import pygame, sys
from utils import draw_text
from pygame.locals import *

def instructionsOfGame(screen, font ,mainClock,lg):
    bg = pygame.image.load("./utilsStatics/controles.jpg")
    controlsBg = pygame.image.load("./utilsStatics/controls.png").convert()

    running = True
    while running:

        if lg == True: 
            screen.blit(controlsBg, [0,0])
        if lg == False:
            screen.blit(bg, [0,0])
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)