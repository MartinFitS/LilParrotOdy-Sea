import pygame, sys
 
mainClock = pygame.time.Clock()
WIDTH = 1270
HEIGHT = 720

from pygame.locals import *
from utils import draw_text
from levels import levelsMenu
from instructions import instructionsOfGame
from credits import credits

from level1 import level1

pygame.init()
pygame.display.set_caption('Lil Parrot Odysea')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
 
font = pygame.font.SysFont(None, 100)
font_lifeBarText = pygame.font.SysFont(None, 30)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('Lil Parrot Ody-Sea', font, (255, 255, 255), screen, 350, 40)
 
        mx, my = pygame.mouse.get_pos()
 
        button_game = pygame.Rect(WIDTH//2.5, 300, 250, 50)
        button_instructions = pygame.Rect(WIDTH//2.5, 400, 250, 50)
        button_credits = pygame.Rect(WIDTH//2.5, 500, 250, 50)
        button_lenguage = pygame.Rect(20, 30, 60,50)

        if button_game.collidepoint((mx, my)):
            if click:
                levelsMenu(screen, mainClock)
                #level1(screen,font_lifeBarText, mainClock)
        if button_instructions.collidepoint((mx, my)):
            if click:
                instructionsOfGame(screen , font , mainClock)
        if button_lenguage.collidepoint((mx,my)):
            if click:
                pass
        if button_credits.collidepoint((mx,my)):
            if click:
                credits(screen , font , mainClock)

        pygame.draw.rect(screen, (255, 0, 0), button_game)
        pygame.draw.rect(screen, (255, 0, 0), button_instructions)
        pygame.draw.rect(screen, (255,0,0), button_credits)
        pygame.draw.rect(screen , (255, 0, 0), button_lenguage)
 
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
main_menu()
