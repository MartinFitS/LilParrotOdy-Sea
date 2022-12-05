import pygame, sys

from pygame.locals import *
from utils import draw_text

from level1 import level1
from level2 import level2
from level3 import level3

from utils import pantalla
click = False

def levelsMenu(screen, sound, mainClock,recolect_trash, damageSound,win,go, lg,select_menu,cc,cm,m,music,mainrun,j_contador,audioM,audioP,audioV,audioA):
    global click
    imgBg = pygame.image.load("./levelsBg.png").convert()
    imgFirstLvl = pygame.image.load("./levelsButtons/nv1.png").convert()
    imgSecondLv2 = pygame.image.load("./levelsButtons/nv2.png").convert()
    imgThirdLv3 = pygame.image.load("./levelsButtons/nv3.png").convert()
    bgLevels = pygame.image.load("./levelsButtons/Levels.png").convert()
    bgNiveles = pygame.image.load("./levelsButtons/niveles.png").convert()
    mensaje = pygame.image.load("./utilsStatics/mensaje.png")
    running = True
    while running:

        mx, my = pygame.mouse.get_pos()


        button_LevelOne = pygame.Rect(22, 25, 170, 220)
        button_LevelTwo = pygame.Rect(554, 525, 170, 220)
        button_LevelThree = pygame.Rect(1080, 25, 170, 220)
        if button_LevelOne.collidepoint((mx, my)):
            if click:
                sound.play()
                level1(screen, pygame.font.SysFont("pixelmix normal", 30),  mainClock,recolect_trash, damageSound,win,go, lg,select_menu,cc,cm,m,music,j_contador)
        if button_LevelTwo.collidepoint((mx,my)):
            if click:
                sound.play()
                level2(screen , pygame.font.SysFont("pixelmix normal", 30), mainClock,recolect_trash, damageSound,win,go,lg,select_menu,cc,cm,m,music,j_contador)
        if button_LevelThree.collidepoint((mx,my)):
            if click: 
                sound.play()
                level3(screen , pygame.font.SysFont("pixelmix normal", 30), mainClock,recolect_trash,damageSound,win,go,lg,select_menu,cc,cm,m,music,j_contador,audioM,audioP,audioV,audioA)
                
        

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    select_menu.play()
                    running = False
                    
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if lg == True:
            screen.blit(bgLevels, [0,0])
        if lg == False:
            screen.blit(bgNiveles, [0,0])
        pygame.display.update()
        mainClock.tick(60)