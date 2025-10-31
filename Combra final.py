# pip install pygame atualizado para ver mudanças

import pygame
import time 
import random 

pygame.init()

# Configuração e criação da tela
largura = 600
altura = 600
tela = pygame.display.set_mode((largura, altura))
Acomida = 500
cenario = pygame.image.load('fundo_ flor.png')
pygame.display.set_caption("Jogo da cobrinha")

# Cores da cobrinha e da comida
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
ROXO = (128, 0, 128)
LARANJA = (255, 165, 0)
VERDE = (0, 255, 0)

# Lista com cores disponíveis
cores_disponiveis = [BRANCO, PRETO, AMARELO, VERMELHO, ROXO, LARANJA, VERDE]

# Criar um relógio
clock = pygame.time.Clock()
velocidade = 10

# Tamanho do bloco da cobrinha e do bloco da comida
tamanho_bloco = 20 

# Fonte do texto do jogo
fonte = pygame.font.SysFont(None, 35)

# Função para mostrar pontuação na tela
def mostrar_pontuacao(pontos):
    valor = fonte.render(f"PONTOS QUE GANHEI: {pontos}", True, PRETO)
    tela.blit(valor, [10, 10])

# Função para desenhar a cobra
def desenha_cobra(tela, cobra_lista, tamanho_bloco, cor_da_cobra):
    for x, y in cobra_lista:
        pygame.draw.rect(tela, cor_da_cobra, [x, y, tamanho_bloco, tamanho_bloco])

# Função para gerar comida com posição e cor aleatória
def gerar_nova_comida(largura_tela, Acomida_tela, tamanho_bloco, cores_disponiveis):
    nova_comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
    nova_comida_y = round(random.randrange(0, Acomida_tela - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
    nova_cor_comida = random.choice(cores_disponiveis)
    return nova_comida_x, nova_comida_y, nova_cor_comida

# Função principal do jogo
def jogo():
    x = largura // 2
    y = altura // 2
    x_mudanca = 0
    y_mudanca = 0

    cobra = []
    comprimento_cobra = 1

    cor_cobra_atual = random.choice(cores_disponiveis)

    comida_x, comida_y, cor_comida_atual = gerar_nova_comida(largura, altura, tamanho_bloco, cores_disponiveis)

    fim_de_jogo = False

    while not fim_de_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_d:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_w:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_s:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        x += x_mudanca
        y += y_mudanca

        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_de_jogo = True 
        
        #Fundo da tela
        tela.blit(cenario, (0,0))

        pygame.draw.rect(tela, cor_comida_atual, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca = [x, y]
        cobra.append(cabeca)

        if len(cobra) > comprimento_cobra:
            del cobra[0]

        for bloco in cobra[:-1]:
            if bloco == cabeca:
                fim_de_jogo = True 
        
        desenha_cobra(tela, cobra, tamanho_bloco, cor_cobra_atual)

        mostrar_pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comprimento_cobra += 1 
            cor_cobra_atual = cor_comida_atual
            comida_x, comida_y, cor_comida_atual = gerar_nova_comida(largura, altura, tamanho_bloco, cores_disponiveis)
        
        clock.tick(velocidade)

    tela.fill(BRANCO)
    mensagem = fonte.render(f"GAME OVER, PONTUAÇÃO: {comprimento_cobra - 1}", True, PRETO)
    tela.blit(mensagem, [largura / 6, altura / 3])
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

jogo()
