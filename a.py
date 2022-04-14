import pygame
from pygame.locals import *
from sys import exit

from random import randint

pygame.init()

largura = 640
altura = 480

p_x = largura/2
p_y = altura/2
p_vel = 15

azul_x = largura/2
azul_y = largura/2

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("jogaço")

relogio = pygame.time.Clock()

fonte = pygame.font.SysFont("arial",20,True)

pontos = 0

while True:
    relogio.tick(30)
    tela.fill((0,0,0))

    mensagem = "Pontos: {}".format(pontos)
    text = fonte.render(mensagem,True,(255,255,0))
    for event in pygame.event.get(): #sair
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    # movimentos
    if pygame.key.get_pressed()[K_a]:
        p_x -= p_vel
    if pygame.key.get_pressed()[K_d]:
        p_x += p_vel
    if pygame.key.get_pressed()[K_w]:
        p_y -= p_vel
    if pygame.key.get_pressed()[K_s]:
        p_y += p_vel

    plr = pygame.draw.rect(tela,(255,155,0),(p_x,p_y,20,30))
    azul = pygame.draw.rect(tela,(0,155,255),(azul_x,azul_y,15,15))
    
    if plr.colliderect(azul):
        azul_x = randint(0,largura- azul.width)
        azul_y = randint(0,altura- azul.height)
        pontos += 1

    tela.blit(text,(0,0))
    pygame.display.flip()
