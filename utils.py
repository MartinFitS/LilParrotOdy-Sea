import pygame
from pygame.locals import *

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_shield_bar(screen,x,y,percentage):
    LONGITUD_DE_BARRA = 100
    ANCHURA_DE_BARRA = 10
    fill = (percentage/100)* LONGITUD_DE_BARRA
    border = pygame.Rect(x,y,LONGITUD_DE_BARRA,ANCHURA_DE_BARRA)
    fill = pygame.Rect(x,y,fill,ANCHURA_DE_BARRA)
    pygame.draw.rect(screen,(0,255,0), fill)
    pygame.draw.rect(screen,(255,255,255), border, 2)

def musicFunction(cm,music):
    if cm % 2 == 0 : 
        m = True
        music.stop()
        print(m)
    if cm % 2 == 1 : 
       m = False
       music.play()
       print(m)

click = False

def pause(running,screen,menu_sound,  lg,cc,cm,m,music):
    global click
    paused = True
    cc = cc
    while paused: 
        button_Home = pygame.Rect(605,440, 80, 80)
        button_Lenguaje = pygame.Rect(480,525, 70, 50)
        button_music = pygame.Rect(900, 150, 70,50)

        bg = pygame.image.load("./utilsStatics/pausa2.png")
        bgI = pygame.image.load("./utilsStatics/pause2.png")
        m_f = pygame.image.load("./utilsStatics/mexico.png").convert()
        i_f = pygame.image.load("./utilsStatics/reinoUnido.png").convert()
        sO = pygame.image.load("./utilsStatics/SonidoOn.png").convert()
        sOff = pygame.image.load("./utilsStatics/soundOff.png").convert()
        sO.set_colorkey((255,255,255))
        sOff.set_colorkey((255,255,255))
        
        if lg == True:
            screen.blit(bgI, [250,30])
            screen.blit(i_f, [450,525])
        if lg == False:
            screen.blit(bg, [250,30])
            screen.blit(m_f, [480,525])
        if m == True:
            screen.blit(sOff, [900,150])
        if m == False:
            screen.blit(sO, [900,150])
        mx ,my = pygame.mouse.get_pos()
        pygame.display.flip()

        if button_Home.collidepoint((mx,my)):
            if click:
                menu_sound.play()
                running = False
                from main import main_menu
                main_menu()
        if button_Lenguaje.collidepoint((mx,my)):
            if click:
                cc = cc + 1
                menu_sound.play()
                if cc % 2 == 0:
                    lg =True
                if cc % 2 != 0:
                    lg = False
                print(cc,lg)
        if button_music.collidepoint((mx,my)):
            if click: 
                cm = cm + 1
                if cm % 2 == 0 : 
                    m = True
                    music.stop()
                    print(m)
                if cm % 2 == 1 : 
                    m = False
                    music.play()
                    print("0ff")

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:        
                paused = False
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

def youWinLvl1Easy(screen, font,mainClock):
   
    screen.fill((0,0,0))
    draw_text('Ganaste el nivel facil', font, (255, 255, 255), screen, 550, 40)
    draw_text('Presiona la tecla enter para jugar el nivel dificil', font, (255, 255, 255), screen, 550, 80)
    pygame.display.flip()
    waiting = True
    while waiting:
        mainClock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     
                if event.key == pygame.K_SPACE:
                    waiting = False

def pantalla(screen,img, mainClock):
    screen.blit(img, [0,0])
    pygame.display.flip()
    waiting = True
    while waiting:
        mainClock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     
                if event.key == pygame.K_ESCAPE:
                    waiting = False

def youLooseLvl1(screen,mainClock):
    bg = pygame.image.load("./utilsStatics/gonivel1.png")
    screen.blit(bg, [0,0])
    pygame.display.flip()
    waiting = True
    while waiting:
        mainClock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     
                if event.key == pygame.K_ESCAPE:
                    waiting = False

def youLooseLvl2(screen,mainClock):
    bg = pygame.image.load("./utilsStatics/gonivel2.png")
    screen.blit(bg, [0,0])
    pygame.display.flip()
    waiting = True
    while waiting:
        mainClock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     
                if event.key == pygame.K_ESCAPE:
                    waiting = False

def youLooseLvl3(screen,mainClock):
    bg = pygame.image.load("./utilsStatics/gonivel3.png")
    screen.blit(bg, [0,0])
    pygame.display.flip()
    waiting = True
    while waiting:
        mainClock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     
                if event.key == pygame.K_ESCAPE:
                    waiting = False

def youWinLvl1Hard(screen, font,mainClock):
    screen.fill((0,0,0))
    draw_text('Ganaste el nivel Dificil', font, (255, 255, 255), screen, 550, 40)
    draw_text('Presiona la tecla enter para jugar el nivel dificil', font, (255, 255, 255), screen, 550, 80)
    pygame.display.flip()
    waiting = True
    while waiting:
        mainClock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     
                if event.key == pygame.K_SPACE:
                    waiting = False
