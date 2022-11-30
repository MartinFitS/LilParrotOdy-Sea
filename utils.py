import pygame

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

def pause(running):
    paused = True
    while paused: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False

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
