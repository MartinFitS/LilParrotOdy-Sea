import pygame,sys;
from pygame.locals import *
from PlayerSecond import PlayerSecond
from JellyFish import JellyFish
from Shark import Shark
from TrashLvl2 import LataLvl2
from level3 import level3
from utils import draw_shield_bar , pantalla,draw_text,youLooseLvl2,pause

def level2(screen, font, mainClock,recolect_trash,damageSound,win,go,lg,select_menu,cc,cm,m,music,j_contador,audioM,audioP,audioV,audioA):
    g_fd = pygame.image.load("./utilsStatics/debajodeloceano2.png").convert()
    g_sd = pygame.image.load("./utilsStatics/debajodeloceano.png").convert()

    w_fd = pygame.image.load("./utilsStatics/under the sea.png").convert()
    w_sd = pygame.image.load("./utilsStatics/under the sea 2.png").convert()

    consejoLv2 = pygame.image.load("./consejos/consejo lv2.png").convert()
    adviceLv2 = pygame.image.load("./consejos/advice lv2.png").convert()

    running = True
    bgS = []
    animationBg = True

    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano2.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano3.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano4.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano5.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano6.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano7.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano8.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano9.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano10.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano11.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano12.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano13.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano14.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano15.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano16.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano17.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano18.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano19.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano20.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano21.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano22.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano23.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel2/debajodeloceano24.png").convert())

    currentBg = 0
    image = bgS[currentBg]

    game_over = True

    while running: 
        if game_over:

            game_over = False
            if lg == False:
                pantalla(screen, consejoLv2, mainClock)
            if lg == True:
                pantalla(screen, adviceLv2, mainClock)

            all_sprites = pygame.sprite.Group()
            jellyFishes_list = pygame.sprite.Group()
            sharks_list = pygame.sprite.Group()
            lata_list = pygame.sprite.Group()

            score = 0
            player = PlayerSecond()
            all_sprites.add(player)

            for i in range(7):
                jellyFish = JellyFish()
                all_sprites.add(jellyFish)
                jellyFishes_list.add(jellyFish) 

            for i in range(4):
                shark = Shark()
                all_sprites.add(shark)
                sharks_list.add(shark) 
            for i in range(3):
                lata = LataLvl2()
                all_sprites.add(lata)
                lata_list.add(lata)

        if animationBg == True:
            currentBg += 0.10
        if int(currentBg) >= len(bgS):
                currentBg = 0
        if animationBg == True:
                image = bgS[int(currentBg)]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause(running,screen,select_menu,lg,cc,cm,m,music,j_contador)
            

        all_sprites.update()

        hitsSL = pygame.sprite.spritecollide(player, sharks_list, True)

        for hit in hitsSL:
            damageSound.play()
            player.lifes -= 75
            shark = Shark()
            all_sprites.add(shark)
            sharks_list.add(shark)

        hitsJL = pygame.sprite.spritecollide(player, jellyFishes_list, True)

        for hit in hitsJL:
            damageSound.play()
            player.lifes -= 25
            jellyFish = JellyFish()
            all_sprites.add(jellyFish)
            jellyFishes_list.add(jellyFish)
           
        hitsTL = pygame.sprite.spritecollide(player, lata_list, True)

        for hit in hitsTL:
            recolect_trash.play()
            score += 1
            lata = LataLvl2()
            all_sprites.add(lata)
            lata_list.add(lata)
        
        if player.lifes <= 0:
            go.play()
            youLooseLvl2(screen, mainClock)
            game_over = True

        if score == 15:
            win.play()
            if lg == False: 
                pantalla(screen, g_fd , mainClock)
            if lg == True:
                pantalla(screen, w_fd , mainClock)
            player.lifes = 100
            score = 16

            for i in range(5):
                jellyFish = JellyFish()
                all_sprites.add(jellyFish)
                jellyFishes_list.add(jellyFish) 

            for i in range(3):
                shark = Shark()
                all_sprites.add(shark)
                sharks_list.add(shark) 

            for i in range(3):
                lata = LataLvl2()
                all_sprites.add(lata)
                lata_list.add(lata)

        if score == 30:
            win.play()
            if lg == False: 
                pantalla(screen, g_sd , mainClock)
            if lg == True:
                pantalla(screen, w_sd , mainClock)
            level3(screen, font, mainClock,recolect_trash,damageSound,win,go,lg,select_menu,cc,cm,m,music,j_contador,audioM,audioP,audioV,audioA)

        

        screen.blit(image, [0,0])
        all_sprites.draw(screen)

        if lg == False:
            draw_text('Puntaje: ', font, (0, 0, 0), screen, 1280//2-50, 10)
            draw_text(str(score), font, (0, 0, 0), screen,  1280//2+50, 10)
            draw_text('Barra de vida: ', font, (0, 0, 0), screen, 10, 10)
            draw_shield_bar(screen, 160,15, player.lifes)
        if lg == True:
            draw_text('Score: ', font, (0, 0, 0), screen, 1280//2-50, 10)
            draw_text(str(score), font, (0, 0, 0), screen,  1280//2+50, 10)
            draw_text('Life: ', font, (0, 0, 0), screen, 10, 10)
            draw_shield_bar(screen, 160,15, player.lifes)

        pygame.display.update()
        mainClock.tick(60)
        pygame.display.flip()
    pygame.quit()
