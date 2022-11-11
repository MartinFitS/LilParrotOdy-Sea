import pygame,sys;
from PlayerSecond import PlayerSecond
from JellyFish import JellyFish
from Shark import Shark
from utils import draw_shield_bar , draw_text

def level2(screen, font, mainClock):
    backgroundlv1 = pygame.image.load("./backgrounds/background_level1.jpeg").convert()
    running = True
    game_over = True

    while running: 
        if game_over:

            game_over = False

            all_sprites = pygame.sprite.Group()
            jellyFishes_list = pygame.sprite.Group()
            sharks_list = pygame.sprite.Group()

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

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        all_sprites.update()
           

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
