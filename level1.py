import pygame,sys
from pygame.locals import *
from Player import Player
from Trash import Basura, Lata , Botella, Erizo
from Kids import Ninos
from utils import draw_shield_bar , draw_text

def level1(screen, font, mainClock):
    backgroundlv1 = pygame.image.load("./backgrounds/background_level1.jpeg").convert()
    running = True
    game_over  = True

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
            for i in range(5):
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
            if player.lifes <= 0:
                pass

        hitsPe = pygame.sprite.spritecollide(player,erizo_list, True)

        for hit in hitsPe: 
            player.lifes -= 50
            erizo = Erizo()
            all_sprites.add(erizo)
            erizo_list.add(erizo)
            if player.lifes <= 0:
                pass
            
        hitsPb = pygame.sprite.spritecollide(player, basura_list, True)

        for hit in hitsPb:
            score += 1  
            if score == 10:
                running = False

        hitsPL = pygame.sprite.spritecollide(player, lata_list, True)

        for hit in hitsPL:
            score += 1  
            if score == 10:
                you_win = True
                running = False

        hitsPBA = pygame.sprite.spritecollide(player, botella_list, True)

        for hit in hitsPBA:
            score += 1  
            if score == 10:
                running = False
           

        screen.blit(backgroundlv1, [0,0])
        all_sprites.draw(screen)

        draw_text('Puntaje: ', font, (255, 255, 255), screen, 1280//2-50, 10)
        draw_text(str(score), font, (255, 255, 255), screen,  1280//2+50, 10)

        draw_text('Barra de vida: ', font, (255, 255, 255), screen, 10, 10)
        draw_shield_bar(screen, 160,15, player.lifes)

        pygame.display.update()
        mainClock.tick(60)
        pygame.display.flip()
    pygame.quit()
