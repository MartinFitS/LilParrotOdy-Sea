import pygame, sys

from pygame.locals import *
from utils import draw_text

from level1 import level1
from level2 import level2

click = False

def levelsMenu(screen,  mainClock):
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Levels', pygame.font.SysFont(None, 100), (255, 255, 255), screen, 1280//2-100, 30)

        mx, my = pygame.mouse.get_pos()


        button_LevelOne = pygame.Rect(370, 250, 250, 300)
        button_LevelTwo = pygame.Rect(670, 250, 250, 300)

        if button_LevelOne.collidepoint((mx, my)):
            if click:
                level1(screen, pygame.font.SysFont(None, 30),  mainClock)
        if button_LevelTwo.collidepoint((mx,my)):
            if click:
                level2(screen , pygame.font.SysFont(None, 30), mainClock)
                
        pygame.draw.rect(screen, (255, 0, 0), button_LevelOne)
        pygame.draw.rect(screen, (255, 0, 0), button_LevelTwo)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)