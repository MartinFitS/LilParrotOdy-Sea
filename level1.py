import pygame,sys
from pygame.locals import *
from Player import Player
from Trash import Basura, Lata , Botella, Erizo
from Kids import Ninos
from utils import draw_shield_bar , draw_text, youWinLvl1Easy,youWinLvl1Hard


def level1(screen, font, mainClock):
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
            ninos_list = pygame.sprite.Group()
            basura_list = pygame.sprite.Group()
            lata_list = pygame.sprite.Group()
            erizo_list = pygame.sprite.Group()
            botella_list = pygame.sprite.Group()
            score = 0
            player = Player()
            all_sprites.add(player)
            
            for i in range(4):
                basura = Basura()
                all_sprites.add(basura)
                basura_list.add(basura)
            for i in range(10):
                erizo = Erizo()
                all_sprites.add(erizo)
                erizo_list.add(erizo)
            for i in range(3):
                lata = Lata()
                all_sprites.add(lata)
                lata_list.add(lata)
            for i in range(3):
                botella = Botella()
                all_sprites.add(botella)
                lata_list.add(botella)
            for i in range(3):
                ninos = Ninos()
                all_sprites.add(ninos)
                ninos_list.add(ninos)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        all_sprites.update()

        hitsNp = pygame.sprite.spritecollide(player, ninos_list, True)

        for hit in hitsNp:
            player.lifes -= 25
            ninos = Ninos()
            all_sprites.add(ninos)
            ninos_list.add(ninos)
            

        hitsPe = pygame.sprite.spritecollide(player,erizo_list, True)

        for hit in hitsPe: 
            player.lifes -= 50
            erizo = Erizo()
            all_sprites.add(erizo)
            erizo_list.add(erizo)
            
            
        hitsPb = pygame.sprite.spritecollide(player, basura_list, True)

        for hit in hitsPb:
            score += 1  
        
        hitsPL = pygame.sprite.spritecollide(player, lata_list, True)

        for hit in hitsPL:
            score += 1  
        
        hitsPBA = pygame.sprite.spritecollide(player, botella_list, True)

        for hit in hitsPBA:
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
            for i in range(8):
                erizo = Erizo()
                all_sprites.add(erizo)
                erizo_list.add(erizo)
            for i in range(8):
                lata = Lata()
                all_sprites.add(lata)
                lata_list.add(lata)
            for i in range(3):
                botella = Botella()
                all_sprites.add(botella)
                lata_list.add(botella)
            for i in range(5):
                ninos = Ninos()
                all_sprites.add(ninos)
                ninos_list.add(ninos)
            
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
