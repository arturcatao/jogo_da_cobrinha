import pygame
from pygame.locals import *
from sys import exit
from random import randint

branco = [255, 255, 255]
preto = [0, 0, 0]
vermelho = [255, 0, 0]
verde = [0, 255, 0]

def mudar_cor(pontos, cor_fonte, cor_tela, cor_cobra, cor_maca):
    if pontos > 2: 
        cor_tela[:] = branco
        cor_cobra[:] = vermelho
        cor_fonte[:] = preto
        cor_maca[:] = verde
    if pontos > 50:
        cor_tela[:] = preto
        cor_cobra[:] = branco
        cor_fonte[:] = branco
        cor_maca[:] = branco

    return cor_fonte, cor_cobra, cor_tela

def limpar_cache():
    for root, dirs, files in os.walk('.'):
        if '__pycache__' in dirs:
            shutil.rmtree(os.path.join(root, '__pycache__'))

