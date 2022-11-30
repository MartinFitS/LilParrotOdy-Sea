import pygame, sys
  
mainClock = pygame.time.Clock()
WIDTH = 1270
HEIGHT = 720

from pygame.locals import *
from levels import levelsMenu
from instructions import instructionsOfGame
from credits import credits

pygame.init()
pygame.display.set_caption('Lil Parrot Odysea')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)

font = pygame.font.SysFont("pixelmix", 100)
font_lifeBarText = pygame.font.SysFont("pixelmix", 30)

music = pygame.mixer.Sound("./sounds/lilparrotSong.mp3")
select_menu = pygame.mixer.Sound("./sounds/select_menuSound.mp3")
recolect_trash = pygame.mixer.Sound("./sounds/recolectSound.wav")
damage_sound = pygame.mixer.Sound("./sounds/damageSound.wav")
win = pygame.mixer.Sound("./sounds/winlvl.wav")
go = pygame.mixer.Sound("./sounds/gameOver.wav")

click = False
 
def main_menu():
    global click
    cc = 1
    lg = False
    bg = pygame.image.load("./bg.png").convert()
    btn_jugar = pygame.image.load("./botonesMenu/JUGAR.png").convert()
    btn_play = pygame.image.load("./utilsStatics/PLAY.png").convert()
    btn_ajustes = pygame.image.load("./botonesMenu/OPCIONES.png").convert()
    btn_settings = pygame.image.load("./utilsStatics/SETTINGS.png").convert()
    while True:     
        # music.play()

        mx, my = pygame.mouse.get_pos()
 
        button_game = pygame.Rect(WIDTH//2.5, 325, 300, 80)
        button_instructions = pygame.Rect(WIDTH//2.5, 435, 300, 80)
        button_credits = pygame.Rect(WIDTH//2.5, 550, 300, 80)
        button_lenguage = pygame.Rect(20, 40, 70,50)
        
        if button_game.collidepoint((mx, my)):
            if click:
                select_menu.play()
                levelsMenu(screen, select_menu, mainClock, recolect_trash,damage_sound,win, go,lg)
        if button_instructions.collidepoint((mx, my)):
            if click:
                select_menu.play()
                instructionsOfGame(screen , font , mainClock)
        if button_lenguage.collidepoint((mx,my)):
            if click:
                select_menu.play()
                cc = cc + 1
                if cc % 2 == 0:
                    lg =True
                if cc % 2 != 0:
                    lg = False
        if button_credits.collidepoint((mx,my)):
            if click:
                credits(screen , font , mainClock)

        pygame.draw.rect(screen, (255, 0, 0), button_game)
        pygame.draw.rect(screen, (255, 0, 0), button_instructions)
        pygame.draw.rect(screen, (255,0,0), button_credits)
        
 
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    select_menu.play()
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        screen.blit(bg, [0,0])
        screen.blit(btn_jugar, [WIDTH//2.5, 325])
        screen.blit(btn_ajustes, [WIDTH//2.5, 435])
        if lg == True:
            screen.blit(btn_play, [WIDTH//2.5, 325])
            screen.blit(btn_settings, [WIDTH//2.5, 435])
        pygame.draw.rect(screen , (255, 0, 0), button_lenguage)
        pygame.display.update()
        mainClock.tick(60)
main_menu()
