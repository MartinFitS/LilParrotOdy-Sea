import pygame,random
from pygame.locals import *

class BlueCrabs(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animation = False
        self.sprites = []


        self.sprites.append(pygame.image.load("./crabsSkins/cangrejoA2.png").convert())
        self.sprites.append(pygame.image.load("./crabsSkins/cangrejoA3.png").convert())
        self.sprites.append(pygame.image.load("./crabsSkins/cangrejoA4.png").convert())
        self.sprites.append(pygame.image.load("./crabsSkins/cangrejoA5.png").convert())
        self.sprites.append(pygame.image.load("./crabsSkins/cangrejoA6.png").convert())

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
      
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(1280 - self.rect.width)
        self.rect.y = random.randrange(550, 700)
        self.speedx = random.randrange(1,6)

    def moving(self):
        self.animation = True

    def update(self):  
        if self.animation == True:
            self.current_sprite += 0.25
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.animationDown = False

        if self.animation == True:
            self.image = self.sprites[int(self.current_sprite)]

        self.rect.x += self.speedx

        self.moving()
        self.image.set_colorkey((0,0,0))

        if self.rect.right > 1280:
            self.speedx *= -1
                   
        if self.rect.left < 0:
            self.speedx *= -1