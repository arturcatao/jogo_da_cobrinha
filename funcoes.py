import pygame
from pygame.locals import *
from sys import exit
from random import randint

pontos = 0
comprimento_inicial = 5
x_cobra = 0
y_cobra = 0
lista_cabeca = []
lista_cobra = []
x_maca = 0
y_maca = 0
morreu = True
branco = [255, 255, 255]
preto = [0, 0, 0]
morreu = True

def maca_falsa():
    pass

def cobra_falsa():
    pass


def mudar_cor(pontos, cor_fonte, cor_tela, cor_cobra, cor_maca):
    if pontos > 20: 
        cor_tela[:] = preto
        cor_cobra[:] = branco
        cor_fonte[:] = branco
    if pontos > 30:
        cor_tela[:]
        cor_cobra[:]
        cor_fonte[:]
        
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
    global morreu
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

