import pygame
from pygame.locals import *
from sys import exit

from random import randrange

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("dinossauro")

relogio = pygame.time.Clock()

sheet = pygame.image.load("Dino.png").convert_alpha()

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(3):
            self.sprites.append( sheet.subsurface( (i*16,0),(16,16) ))
            
        self.frame = 0
        self.image = self.sprites[int(self.frame)]
        self.rect = self.image.get_rect()
        self.rect.topleft = (100,altura-128)

        self.pulo = False
        self.vector_y = 0
        self.chao = self.rect.y
        
    def pular(self):
        self.pulo = True
        self.vector_y = 20
        
    def update(self):
        if self.frame > 2:
            self.frame = 0
            
        self.frame += 0.1
        self.image = self.sprites[int(self.frame)]
        self.image = pygame.transform.scale(self.image,(64,64))

        if self.pulo:
            if self.rect.y <= self.chao:
                self.rect.y = min(self.rect.y-self.vector_y , self.chao)
                self.vector_y -= 2
                
            elif self.rect.y > self.chao:
                self.pulo = False
                self.rect.y = self.chao
            

class Nuvem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sheet.subsurface((7*16,0),(16,16))
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()
        #self.rect.center = (largura,)
        self.rect.y = randrange(0,200,50)
        self.rect.x = largura + randrange(0,600,90)
    def update(self):
        self.rect.x -= 10
        if self.rect.topright[0] < 0:
            self.rect.y = randrange(0,200,50)
            self.rect.x = largura + randrange(0,600,90)


class Chao(pygame.sprite.Sprite):
    def __init__(self,px):
        pygame.sprite.Sprite.__init__(self)
        self.image = sheet.subsurface((6*16,0),(16,16))
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()
        self.rect.y = altura - 64
        self.rect.x = px*64
    def update(self):
        self.rect.x -= 10
        if self.rect.topright[0] < 0:
            self.rect.x += largura+64

class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sheet.subsurface((5*16,0),(16,16))
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (largura,altura-64)
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        self.rect.x -= 10
        if self.rect.topright[0] < 0:
            self.rect.x += largura+64

all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()

dino = Dino()
all_sprites.add(dino)

for i in range(2):
    nuvem = Nuvem()
    all_sprites.add(nuvem)

for i in range(11):
    chao = Chao(i)
    all_sprites.add(chao)

cacto = Cacto()
all_sprites.add(cacto)
all_enemies.add(cacto)

while True:
    relogio.tick(30)
    
    tela.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and dino.rect.y == dino.chao:
                dino.pular()

    colisoes = pygame.sprite.spritecollide(dino,all_enemies,False,pygame.sprite.collide_mask)


    all_sprites.draw(tela)
    if colisoes:
        pass
    else:
        all_sprites.update() #bagulho das animações
    
    pygame.display.flip()
