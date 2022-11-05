import pygame, random
from pygame.locals import *

#Creamos la clase basura                  
class Basura(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./basura/botella.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1280 - self.rect.width)
        self.rect.y = random.randrange(300, 400)
#Creamos la clase lata 
class Lata(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./basura/lata.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1280 - self.rect.width)
        self.rect.y = random.randrange(300, 400)
#Creamos la clase botella 
class Botella(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./basura/botelladeagua.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1280 - self.rect.width)
        self.rect.y = random.randrange(300, 400)
#Creamos la clase erizo 
class Erizo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./basura/erizo.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1280 - self.rect.width)
        self.rect.y = random.randrange(300, 400)