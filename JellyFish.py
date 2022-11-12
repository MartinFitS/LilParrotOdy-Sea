import pygame,random
from pygame.locals import *

class JellyFish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animation = False
        self.sprites = []

        self.sprites.append(pygame.image.load("./jellyFishSkins/medusa1.png").convert())
        self.sprites.append(pygame.image.load("./jellyFishSkins/medusa2.png").convert())
        self.sprites.append(pygame.image.load("./jellyFishSkins/medusa3.png").convert())
        self.sprites.append(pygame.image.load("./jellyFishSkins/medusa4.png").convert())
        self.sprites.append(pygame.image.load("./jellyFishSkins/medusa5.png").convert())
        self.sprites.append(pygame.image.load("./jellyFishSkins/medusa6.png").convert())


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(500, 1200)
        self.rect.y = random.randrange(50 , 650)
        self.speedx = random.randrange(3,5)
        self.speedy = random.randrange(-5, 5)
        
    def moving(self):
        self.animation = True

    def update(self):
        self.image.set_colorkey((0,0,0))   
  
        if self.animation == True:
            self.current_sprite += 0.25
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.animation = False

        if self.animation == True:
            self.image = self.sprites[int(self.current_sprite)]

        self.rect.x -= self.speedx
        self.rect.y -= self.speedy

        
        self.moving()
        if self.rect.top > 1280 + 10 or self.rect.left < -25 or self.rect.right > 1280 +25:
            self.rect.x = random.randrange(500,1200)
            self.rect.y = random.randrange(50 , 650)
            self.speedx = random.randrange(1,5)