import pygame
from pygame.locals import *
from sys import exit
from random import randint
from funcoes import *
import os

'''
adicionar maçã falsa
fazer com q quando bata na parede a cobra morra
ajeitar a função game over que não ta reinicializando o jogo
'''

pygame.init()

caminho_do_arquivo = 'pycash'

largura = 640 
altura = 480

x_cobra = int(largura/2) 
y_cobra = int(altura/2)

velocidade = 10

x_controle = velocidade
y_controle = 0


x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

vermelho = [255, 0, 0]
branco = [255, 255, 255]
preto = [0, 0, 0]
cor_fonte = preto
cor_tela = branco
cor_cobra = [0, 255, 0]
cor_maca = vermelho


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y

        pygame.draw.rect(tela, (cor_cobra[0],cor_cobra[1],cor_cobra[2]), (XeY[0], XeY[1], 20, 20))

while True:
    relogio.tick(30)
    tela.fill((cor_tela[0],cor_tela[1],cor_tela[2]))

    mudar_cor(pontos, cor_fonte, cor_tela, cor_cobra, cor_maca)
    
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (cor_fonte[0],cor_fonte[1],cor_fonte[2]))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            
            if os.path.exists(caminho_do_arquivo):
                os.remove(caminho_do_arquivo)
                print(f'O arquivo {caminho_do_arquivo} foi apagado com sucesso.')
            else:
                print(f'O arquivo {caminho_do_arquivo} não existe.')
            
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
        
    cobra = pygame.draw.rect(tela, (cor_cobra[0],cor_cobra[1],cor_cobra[2]), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (cor_maca[0], cor_maca[1], cor_maca[2]), (x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        comprimento_inicial = comprimento_inicial + 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        game_over(tela, largura, altura)

    '''
    esse bloco tem que ser substituido pq quando bate na parede tem que morrer
    e não voltar do outro lado'''
    
    
    if x_cobra > largura:
        game_over(tela, largura, altura)
    if x_cobra < 0:
        game_over(tela, largura, altura)
    if y_cobra < 0:
        game_over(tela, largura, altura)
    if y_cobra > altura:
        game_over(tela, largura, altura)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450,40))

    pygame.display.update()