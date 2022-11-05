import pygame,random
from pygame.locals import *

class Ninos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animationDown = False
        self.animationUp = False
        #Implementamos los sprites
        self.spritesDown = []
        self.spriteUp = []

        self.spritesDown.append(pygame.image.load("./ninos/morro1.png").convert())
        self.spritesDown.append(pygame.image.load("./ninos/morro2.png").convert())
        self.spritesDown.append(pygame.image.load("./ninos/morro3.png").convert())
        self.spritesDown.append(pygame.image.load("./ninos/morro4.png").convert())

        self.spriteUp.append(pygame.image.load("./ninos/morro2espalda1.png").convert())
        self.spriteUp.append(pygame.image.load("./ninos/morro2espalda2.png").convert())
        self.spriteUp.append(pygame.image.load("./ninos/morro2espalda3.png").convert())
        self.spriteUp.append(pygame.image.load("./ninos/morro2espalda4.png").convert())

        self.current_sprite = 0
        self.image = self.spritesDown[self.current_sprite]
        self.imageUp = self.spriteUp[self.current_sprite]
      
        self.rect = self.image.get_rect()
        self.rectAbajo = self.imageUp.get_rect()

        #Definimos la aparicion de los niños de una manera random
        self.rect.x = random.randrange(1280 - self.rect.width)
        self.rect.y = random.randrange(300, 400)
        self.speedy = random.randrange(1,3)

    def movingDown(self):
        self.animationDown = True
    def movingUp(self):
        self.animationUp = True

    #Damos instrucciones de como se mueven los niños, esta vez de manera vertical
    def update(self):  
        self.image.set_colorkey((0,0,0))
        self.imageUp.set_colorkey((0,0,0))
        
        if self.animationDown == True:
            self.current_sprite += 0.25
            if int(self.current_sprite) >= len(self.spritesDown):
                self.current_sprite = 0
                self.animationDown = False
        if self.animationUp == True:
            self.current_sprite += 0.25
            if int(self.current_sprite) >= len(self.spriteUp):
                self.current_sprite = 0
                self.animationUp = False

        if self.animationDown == True:
            self.image = self.spritesDown[int(self.current_sprite)]
        if self.animationUp == True:
            self.image = self.spriteUp[int(self.current_sprite)]

        self.rect.y += self.speedy

        self.movingDown()

        if self.rect.bottom > 720:
            self.movingUp()
            self.animationDown = False
            self.speedy *= -1
            
            
            
        if self.rect.top < 200:
            self.movingDown()
            self.animationUp = False
            self.speedy *= -1