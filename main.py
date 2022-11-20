import pygame, sys
 
mainClock = pygame.time.Clock()
WIDTH = 1270
HEIGHT = 720

from pygame.locals import *
from utils import draw_text
from levels import levelsMenu
from instructions import instructionsOfGame
from credits import credits

pygame.init()
pygame.display.set_caption('Lil Parrot Odysea')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
 
font = pygame.font.SysFont("pixelmix", 100)
font_lifeBarText = pygame.font.SysFont("pixelmix", 30)
 

music = pygame.mixer.Sound("./sounds/lilparrotSong.mp3")
click = False
 
def main_menu():
    global click
    bg = pygame.image.load("./bg.png").convert()
    while True:
        
        music.play()
        screen.blit(bg, [0,0])
        mx, my = pygame.mouse.get_pos()
 
        button_game = pygame.Rect(WIDTH//2.5, 300, 250, 50)
        button_instructions = pygame.Rect(WIDTH//2.5, 400, 250, 50)
        button_credits = pygame.Rect(WIDTH//2.5, 500, 250, 50)
        button_lenguage = pygame.Rect(20, 30, 60,50)
        
        if button_game.collidepoint((mx, my)):
            if click:
                levelsMenu(screen, mainClock)
        if button_instructions.collidepoint((mx, my)):
            if click:
                instructionsOfGame(screen , font , mainClock)
        if button_lenguage.collidepoint((mx,my)):
            if click:
                music.stop()
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
