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
