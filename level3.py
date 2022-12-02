import pygame,random
from pygame.locals import *
from PlayerThird import Player
from Trash import Basura
from Crab import Crabs
from BlueCrabs import BlueCrabs
from utils import draw_shield_bar , draw_text,pantalla,youLooseLvl3,pause

def level3(screen, font, mainClock,recolect_trash,damageSound,win,go,lg,select_menu,cc,cm,m,music):
    g_fd = pygame.image.load("./utilsStatics/muelle1.png").convert()
    g_sd = pygame.image.load("./utilsStatics/muelle2.png").convert()

    w_fd = pygame.image.load("./utilsStatics/dock.png").convert()
    w_sd = pygame.image.load("./utilsStatics/dock2.png").convert()

    consejoLv3 = pygame.image.load("./consejos/consejo lv3.png").convert()
    adviceLv3 = pygame.image.load("./consejos/advice lv3.png").convert()

    running = True
    game_over  = True
    bgS = []
    animationBg = True

    bgS.append(pygame.image.load("./backgroundLevel3/muelle1.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel3/muelle2.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel3/muelle3.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel3/muelle4.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel3/muelle5.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel3/muelle6.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel3/muelle7.png").convert())
    bgS.append(pygame.image.load("./backgroundLevel3/muelle8.png").convert())
    
    currentBg = 0
    image = bgS[currentBg]

    while running: 
        if game_over:

            game_over = False
            if lg == False:
                pantalla(screen, consejoLv3, mainClock)
            if lg == True:
                pantalla(screen, adviceLv3, mainClock)
            all_sprites = pygame.sprite.Group()
            basura_list = pygame.sprite.Group()
            crabs_list = pygame.sprite.Group()
            blueCrabs = pygame.sprite.Group()

            score = 0
            player = Player()
            all_sprites.add(player)
            
            for i in range(10):
                basura = Basura()
                basura.rect.x = random.randrange(240 + basura.rect.width, 1050 - basura.rect.width)
                basura.rect.y = random.randrange(0 + basura.rect.height, 680 - basura.rect.height)
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
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause(running,screen,select_menu,lg,cc,cm,m,music)
            

        all_sprites.update()

        hitsPCR = pygame.sprite.spritecollide(player, crabs_list, True)

        for hit in hitsPCR:
            damageSound.play()
            player.lifes -= 25

        hitsPCA = pygame.sprite.spritecollide(player, blueCrabs, True)

        for hit in hitsPCA:
            damageSound.play()
            player.lifes -= 50

        hitsPb = pygame.sprite.spritecollide(player, basura_list, True)

        for hit in hitsPb:
            recolect_trash.play()
            score += 1  
        
           
        if animationBg == True:
            currentBg += 0.10
        if int(currentBg) >= len(bgS):
                currentBg = 0
        if animationBg == True:
                image = bgS[int(currentBg)]

        if player.lifes <= 0:
            go.play()
            youLooseLvl3(screen, mainClock)
            game_over = True

        if score == 10:
            win.play()
            if lg == False: 
                pantalla(screen, g_fd , mainClock)
            if lg == True:
                pantalla(screen, w_fd , mainClock)
            player.lifes = 100
            score = 11
            
            for i in range(14):
                basura = Basura()
                basura.rect.x = random.randrange(240 + basura.rect.width, 1050 - basura.rect.width)
                basura.rect.y = random.randrange(0 + basura.rect.height, 680 - basura.rect.height)
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
                     
        if score == 25:
            win.play()
            if lg == True:
                pantalla(screen, w_sd , mainClock)
                running = False
                from main import main_menu
            if lg == False:
                pantalla(screen, g_sd , mainClock)
                running = False
                from main import main_menu
                main_menu()

            
            
        screen.blit(image, [0,0])
        all_sprites.draw(screen)

        if lg == False:
            draw_text('Puntaje: ', font, (255, 255, 255), screen, 1280//2-50, 10)
            draw_text(str(score), font, (255, 255, 255), screen,  1280//2+50, 10)
            draw_text('Barra de vida: ', font, (255, 255, 255), screen, 10, 10)
            draw_shield_bar(screen, 160,15, player.lifes)
        if lg == True:
            draw_text('Score: ', font, (255, 255, 255), screen, 1280//2-50, 10)
            draw_text(str(score), font, (255, 255, 255), screen,  1280//2+50, 10)
            draw_text('Life: ', font, (255, 255, 255), screen, 10, 10)
            draw_shield_bar(screen, 160,15, player.lifes)

        pygame.display.update()
        mainClock.tick(60)
        pygame.display.flip()
    pygame.quit()

