import pygame
from pygame.locals import *
from Player import Player
from Trash import Basura
from Crab import Crabs
from BlueCrabs import BlueCrabs
from utils import draw_shield_bar , draw_text, youWinLvl1Easy,youWinLvl1Hard

def level3(screen, font, mainClock):
    running = True
    game_over  = True
    bgS = []
    animationBg = True

    bgS.append(pygame.image.load("./backgroundLevel1/playa1.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel1/playa2.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel1/playa3.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel1/playa4.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel1/playa5.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel1/playa6.png").convert())
    
    currentBg = 0
    image = bgS[currentBg]

    while running: 
        if game_over:

            game_over = False

            all_sprites = pygame.sprite.Group()
            basura_list = pygame.sprite.Group()
            crabs_list = pygame.sprite.Group()
            blueCrabs = pygame.sprite.Group()

            score = 0
            player = Player()
            all_sprites.add(player)
            
            for i in range(4):
                basura = Basura()
                all_sprites.add(basura)
                basura_list.add(basura)
            
            for i in range(5):
                crab = Crabs()
                all_sprites.add(crab)
                crabs_list.add(crab)
            
            for i in range(3):
                blueCrab = BlueCrabs()
                all_sprites.add(blueCrab)
                blueCrabs.add(blueCrab)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        all_sprites.update()

        
        hitsPb = pygame.sprite.spritecollide(player, basura_list, True)

        for hit in hitsPb:
            score += 1  
        
           
        if animationBg == True:
            currentBg += 0.10
        if int(currentBg) >= len(bgS):
                currentBg = 0
        if animationBg == True:
                image = bgS[int(currentBg)]

        if player.lifes <= 0:
            youWinLvl1Easy(screen, font, mainClock)
            game_over = True

        if score == 10:
            youWinLvl1Easy(screen, font, mainClock)
            player.lifes = 100
            score = 10
            
            for i in range(9):
                basura = Basura()
                all_sprites.add(basura)
                basura_list.add(basura)
            
        if score == 25:
            youWinLvl1Hard(screen, font, mainClock)
            
            
        screen.blit(image, [0,0])
        all_sprites.draw(screen)

        draw_text('Puntaje: ', font, (255, 255, 255), screen, 1280//2-50, 10)
        draw_text(str(score), font, (255, 255, 255), screen,  1280//2+50, 10)

        draw_text('Barra de vida: ', font, (255, 255, 255), screen, 10, 10)
        draw_shield_bar(screen, 160,15, player.lifes)

        pygame.display.update()
        mainClock.tick(60)
        pygame.display.flip()
    pygame.quit()

