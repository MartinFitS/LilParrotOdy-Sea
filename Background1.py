import pygame
from pygame.locals import *

class B1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sprites = []
        self.animation = True
        self.sprites.append(pygame.image.load("./backgroundLevel1/playa1.png").convert())
        self.sprites.append(pygame.image.load("./backgroundLevel1/playa2.png").convert())
        self.sprites.append(pygame.image.load("./backgroundLevel1/playa3.png").convert())
        self.sprites.append(pygame.image.load("./backgroundLevel1/playa4.png").convert())
        self.sprites.append(pygame.image.load("./backgroundLevel1/playa5.png").convert())
        self.sprites.append(pygame.image.load("./backgroundLevel1/playa6.png").convert())

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def update(self):
        self.image.set_colorkey((0,0,0))

        if self.animation == True:
            self.current_sprite += 0.25
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.animation = False

        if self.animation == True:
            self.image = self.sprites[int(self.current_sprite)]
        
  
        return self.image