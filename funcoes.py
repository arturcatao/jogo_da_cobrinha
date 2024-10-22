import pygame
from pygame.locals import *
from sys import exit
from random import randint

branco = [255, 255, 255]
preto = [0, 0, 0]
vermelho = [255, 0, 0]
verde = [0, 255, 0]

"""def maca_falsa(tela, cor_maca, pontos): # ta dando loop n sei pq
    x_maca_fake = randint(40, 600)
    y_maca_fake = randint(50, 430)
    
    if pontos > 5:
        #fazer com que quando a maça seja comida as duas sumam e vice e versa
        maca_fake = pygame.draw.rect(tela, (cor_maca[0], cor_maca[1], cor_maca[2]), (x_maca_fake,y_maca_fake,20,20))"""


def cobra_falsa():
    pass


def mudar_cor(pontos, cor_fonte, cor_tela, cor_cobra, cor_maca):
    if pontos > 20: 
        cor_tela[:] = preto
        cor_cobra[:] = branco
        cor_fonte[:] = branco
        cor_maca[:] = branco
    if pontos > 30:
        cor_tela[:] = branco
        cor_cobra[:] = vermelho
        cor_fonte[:] = preto
        cor_maca[:] = verde

    return cor_fonte, cor_cobra, cor_tela

