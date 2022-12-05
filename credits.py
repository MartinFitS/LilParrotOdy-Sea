import pygame, sys
from utils import draw_text
from pygame.locals import *
click = False
def credits(screen, mainClock,lg,j_contador,music,m,select_menu,audioM,audioP,audioV,audioA):
    global click
    efi = pygame.image.load("./utilsStatics/credits.png").convert()
    efe = pygame.image.load("./utilsStatics/creditos.png").convert()
    menu = pygame.Rect(600, 250, 70,60)
    m_b = pygame.Rect(305, 350, 150,160)
    a_b = pygame.Rect(305, 100, 150,160)
    p_b = pygame.Rect(525, 350, 150,160)
    v_b = pygame.Rect(825, 350, 150,160)
    j_contador = j_contador + 1
    running = True
    
    while running:
        mx ,my = pygame.mouse.get_pos()

        if menu.collidepoint((mx,my)):
            if click:
                select_menu.play()
                music.stop()
                from main import main_menu
                main_menu(j_contador)
        if m_b.collidepoint((mx,my)):
            if click:
                audioM.play()
        if p_b.collidepoint((mx,my)):
            if click:
                audioP.play()
        if v_b.collidepoint((mx,my)):
            if click:
                audioV.play()
        if a_b.collidepoint((mx,my)):
            if click:
                audioA.play()
        click = False
        if lg == True: 
            pygame.draw.rect(screen, (255,255,255), m_b)
            screen.blit(efi, [0,0])
        if lg == False:
            pygame.draw.rect(screen, (255,255,255), m_b)
            screen.blit(efe, [0,0])

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

        pygame.display.update()
        mainClock.tick(60)