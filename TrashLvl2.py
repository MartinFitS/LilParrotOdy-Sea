import pygame, random
from pygame.locals import *

class LataLvl2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./basura/lata.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(500, 1200)
        self.rect.y = random.randrange(50 , 650)
        self.speedx = random.randrange(3,5)

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.top > 1280 + 10 or self.rect.left < -25 or self.rect.right > 1280 +25:
            self.rect.x = random.randrange(900,1200)
            self.rect.y = random.randrange(50 , 650)
            self.speedx = random.randrange(4,7)



