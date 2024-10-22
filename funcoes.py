import pygame
from pygame.locals import *
from sys import exit
from random import randint

branco = [255, 255, 255]
preto = [0, 0, 0]
vermelho = [255, 0, 0]
verde = [0, 255, 0]
morreu = True

"""def maca_falsa(tela, cor_maca, pontos): # ta dando loop n sei pq
    x_maca_fake = randint(40, 600)
    y_maca_fake = randint(50, 430)
    
    if pontos > 5:
        #fazer com que quando a maça seja comida as duas sumam e vice e versa
        maca_fake = pygame.draw.rect(tela, (cor_maca[0], cor_maca[1], cor_maca[2]), (x_maca_fake,y_maca_fake,20,20))
"""    

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

def reiniciar_jogo(largura, altura):
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeca, lista_cobra, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura/2
    y_cobra = altura/2
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False


def game_over(tela, largura, altura):
    global morreu # passei um ano pra entender que so faltava declarar morreu como global pra funcionar
    fonte2 = pygame.font.SysFont("arial", 20, True, True)
    mensagem = "Game Over! R para reiniciar o jogo"
    texto_formatado = fonte2.render(mensagem, True, (0,0,0))
    ret_texto = texto_formatado.get_rect()

    morreu = True
    while morreu:
        tela.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    return reiniciar_jogo(largura, altura)
        ret_texto.center = (largura//2, altura//2)
        tela.blit(texto_formatado, ret_texto)
        pygame.display.update()

