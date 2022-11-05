import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.moving_animation = False
        self.moving_animation_left = False
        #Implementamos los sprites del jugador
        self.sprites = []

        self.sprites.append(pygame.image.load("./lilparrot/loro1.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro2.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro3.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro4.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro5.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro6.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro7.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro8.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro9.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro10.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro11.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro12.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro13.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro14.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro15.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro16.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro17.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro18.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro19.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro20.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro21.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro22.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro23.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro24.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro25.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro26.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro27.png"))
        self.sprites.append(pygame.image.load("./lilparrot/loro28.png"))

        self.srpitesIzq = []

        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves1.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves2.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves3.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves4.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves5.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves6.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves7.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves8.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves9.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves10.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves11.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves12.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves13.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves14.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves15.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves16.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves17.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves18.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves19.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves20.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves21.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves22.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves23.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves24.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves25.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves26.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves27.png"))
        self.srpitesIzq.append(pygame.image.load("./lilparrotIzquierda/loroReves28.png"))
     

        self.current_sprite = 0
        self.current_sprite_Izq = 0
        self.image = self.sprites[self.current_sprite]
        self.imageIzq = self.srpitesIzq[self.current_sprite_Izq]
        self.image.set_colorkey((0,0,0))
        self.imageIzq.set_colorkey((0,0,0))
        self.rectIzq = self.imageIzq.get_rect()
        self.rect = self.image.get_rect()

        self.speed_x = 0
        self.speed_y = 0
        self.rect.centerx = 1280 // 2
        self.rect.bottom = 720 - 10
        self.lifes = 100

    def moving(self):
        self.moving_animation = True

    def movingLeft(self):
        self.moving_animation_left = True
    #Actualizamos las variables de movimiento del jugador, y obtenemos los contyroles mediante las teclas para movernos por el mapa
    #Asi como tambien actualizamos los sprites para que parezca que se animen
    def update(self):
        self.speed_x = 0
        self.speed_y = 0

        if self.moving_animation == True:
            self.current_sprite += 0.5
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.moving_animation = False

        if self.moving_animation_left == True:
            self.current_sprite_Izq += 0.5
            if int(self.current_sprite_Izq) >= len(self.srpitesIzq):
                self.current_sprite_Izq = 0
                self.moving_animation_left = False

        if self.moving_animation == True:
            self.image = self.sprites[int(self.current_sprite)]
        if self.moving_animation_left == True:
            self.image = self.srpitesIzq[int(self.current_sprite_Izq)] 

        keystate = pygame.key.get_pressed()
    
        if keystate[pygame.K_LEFT]:  
            self.movingLeft()
            self.speed_x = -3
            print(self.current_sprite)
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 3
            self.moving()
            
        if keystate[pygame.K_UP]:
            self.speed_y = -3
            self.moving()
        if keystate[pygame.K_DOWN]:
            self.speed_y = 3
            self.moving()

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #Delimitamos donde puede caminar el jugador
        if self.rect.right > 1280:
            self.rect.right = 1280
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > 720:
            self.rect.bottom = 720
        if self.rect.top < 200:         
            self.rect.top = 200