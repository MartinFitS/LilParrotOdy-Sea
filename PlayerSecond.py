import pygame
from pygame.locals import *

class PlayerSecond(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.moving_animation = False

        self.sprites = []

        self.sprites.append(pygame.image.load("./lilparrot/loro1.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro2.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro3.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro4.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro5.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro6.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        self.speed_y = 0
        self.rect.centerx = 80
        self.lifes = 100

    def moving(self):
        self.moving_animation = True

    def update(self):
        self.speed_y = 0

        if self.moving_animation == True:
            self.current_sprite += 0.5
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.moving_animation = False

        if self.moving_animation == True:
            self.image = self.sprites[int(self.current_sprite)]

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_UP]:
            self.speed_y = -3
            print(self.current_sprite)
            self.moving()

        if keystate[pygame.K_DOWN]:
            self.speed_y = 3
            self.moving()

        self.rect.y += self.speed_y

        if self.rect.bottom > 690:
            self.rect.bottom = 690
        if self.rect.top < 64:         
            self.rect.top = 64