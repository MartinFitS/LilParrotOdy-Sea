import pygame, sys

from pygame.locals import *
from utils import draw_text

from level1 import level1
from level2 import level2
from level3 import level3

click = False

def levelsMenu(screen, sound, mainClock,recolect_trash, damageSound,win,go):
    global click
    imgBg = pygame.image.load("./levelsBg.png").convert()
    imgFirstLvl = pygame.image.load("./levelsButtons/nv1.png").convert()
    imgSecondLv2 = pygame.image.load("./levelsButtons/nv2.png").convert()
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Levels', pygame.font.SysFont("pixelmix", 100), (255, 255, 255), screen, 1280//2-100, 30)

        mx, my = pygame.mouse.get_pos()


        button_LevelOne = pygame.Rect(170, 250, 250, 300)
        button_LevelTwo = pygame.Rect(470, 250, 250, 300)
        button_LevelThree = pygame.Rect(770, 250, 250, 300)

        if button_LevelOne.collidepoint((mx, my)):
            if click:
                sound.play()
                level1(screen, pygame.font.SysFont("pixelmix normal", 30),  mainClock,recolect_trash, damageSound,win,go)
        if button_LevelTwo.collidepoint((mx,my)):
            if click:
                sound.play()
                level2(screen , pygame.font.SysFont("pixelmix normal", 30), mainClock,recolect_trash, damageSound,win,go)
        if button_LevelThree.collidepoint((mx,my)):
            if click: 
                sound.play()
                level3(screen , pygame.font.SysFont("pixelmix normal", 30), mainClock)
                
        pygame.draw.rect(screen, (255, 0, 0), button_LevelOne)

        pygame.draw.rect(screen, (255, 0, 0), button_LevelTwo)

        pygame.draw.rect(screen, (255,0,0), button_LevelThree)

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
        screen.blit(imgBg, [0,0])
        screen.blit(imgFirstLvl, [170, 250])
        screen.blit(imgSecondLv2, [470, 250])
        pygame.display.update()
        mainClock.tick(60)