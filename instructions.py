import pygame, sys
from utils import draw_text
from pygame.locals import *

def instructionsOfGame(screen, font ,mainClock):
    bg = pygame.image.load("./utilsStatics/controles.jpg")
    running = True
    while running:
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