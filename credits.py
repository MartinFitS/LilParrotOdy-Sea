import pygame, sys
from utils import draw_text
from pygame.locals import *
click = False
def credits(screen, mainClock,lg,j_contador,music,m):
    global click
    efi = pygame.image.load("./utilsStatics/credits.png").convert()
    efe = pygame.image.load("./utilsStatics/creditos.png").convert()
    menu = pygame.Rect(600, 250, 70,60)
    j_contador = j_contador + 1
    running = True
    
    while running:
        mx ,my = pygame.mouse.get_pos()
        screen.fill((0,0,0))

        if menu.collidepoint((mx,my)):
            if click:
                music.stop()
                from main import main_menu
                main_menu(j_contador)
        click = False
        if lg == True: 
            screen.blit(efi, [0,0])
        if lg == False:
            screen.blit(efe, [0,0])

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