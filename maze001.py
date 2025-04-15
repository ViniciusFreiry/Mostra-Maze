################################################################
###                 M O S T R A   M A Z E                    ###
################################################################
### Neste teste, mostra o labirinto gerado pelo algoritmo de ###
### Aldous-Broder                                            ###
################################################################
### Prof. Filipo Mor, FILIPOMOR.COM                          ###
################################################################

import pygame
import sys
import copy
import random
import heapq
from random import randint

class ArestasFechadas:
    def __init__(self, superior, inferior, esquerda, direita):
        self.superior = superior
        self.inferior = inferior
        self.esquerda = esquerda
        self.direita = direita


class Celula:
    def __init__(self, arestasFechadas, corPreenchimento, corVisitada, corLinha, corAberta, visitada, aberta):
        self.arestasFechadas = arestasFechadas
        self.corPreenchimento = corPreenchimento
        self.corVisitada = corVisitada
        self.corLinha = corLinha
        self.corAberta = corAberta
        self.visited = visitada
        self.aberta = aberta
        self.no_caminho = False

    def get_corPreenchimento(self):
        return self.corPreenchimento

    def get_arestasFechadas(self):
        return self.arestasFechadas

    def is_visited(self):
        return self.visited

    def desenhar(self, tela, x, y, aresta):
        # x : coluna
        # y : linha

        # calcula as posicoes de desenho das linhas de cada aresta
        arSuperiorIni = (x, y)
        arSuperiorFim = (x + aresta, y)
        arInferiorIni = (x, y + aresta)
        arInferiorFim = (x + aresta, y + aresta)
        arEsquerdaIni = (x, y)
        arEsquerdaFim = (x, y + aresta)
        arDireitaIni = (x + aresta, y)
        arDireitaFim = (x + aresta, y + aresta)

        # preenche a célula com a cor definida
        if (self.aberta):
            pygame.draw.rect(tela, self.corAberta, (x, y, aresta, aresta))
        else:
            pygame.draw.rect(tela, self.corPreenchimento, (x, y, aresta, aresta))

        # Verifica se a célula está no caminho
        if self.no_caminho:
            pygame.draw.rect(tela, (0, 255, 0), (x, y, aresta, aresta))  # amarelo
        elif self.aberta:
            pygame.draw.rect(tela, self.corAberta, (x, y, aresta, aresta))
        else:
            pygame.draw.rect(tela, self.corPreenchimento, (x, y, aresta, aresta))

        pygame.draw.line(tela, self.corLinha, arSuperiorIni, arSuperiorFim)
        pygame.draw.line(tela, self.corLinha, arInferiorIni, arInferiorFim)
        pygame.draw.line(tela, self.corLinha, arEsquerdaIni, arEsquerdaFim)
        pygame.draw.line(tela, self.corLinha, arDireitaIni, arDireitaFim)
        
        '''
        # linha superior
        if (self.arestasFechadas.superior):
            pygame.draw.line(tela, self.corLinha, arSuperiorIni, arSuperiorFim)
        # linha inferior
        if (self.arestasFechadas.inferior):
            pygame.draw.line(tela, self.corLinha, arInferiorIni, arInferiorFim)
        # linha esquerda
        if (self.arestasFechadas.esquerda):
            pygame.draw.line(tela, self.corLinha, arEsquerdaIni, arEsquerdaFim)
        # linha direita
        if (self.arestasFechadas.direita):
            pygame.draw.line(tela, self.corLinha, arDireitaIni, arDireitaFim)
        '''
            
        # pygame.draw.line(tela, self.corLinha, arSuperiorIni, arSuperiorFim)
        # pygame.draw.line(tela, self.corLinha, arInferiorIni, arInferiorFim)
        # pygame.draw.line(tela, self.corLinha, arEsquerdaIni, arEsquerdaFim)
        # pygame.draw.line(tela, self.corLinha, arDireitaIni, arDireitaFim)

class AldousBroder:
    def __init__(self, qtLinhas, qtColunas, aresta, celulaPadrao):
        self.matriz = Malha(qtLinhas, qtColunas, aresta, celulaPadrao)
        self.qtLinhas = qtLinhas
        self.qtColunas = qtColunas
        self.aresta = aresta
        self.celulaPadrao = celulaPadrao
        # self.visitados = []

    def __len__(self):
        return len(self.matriz)

    def __iter__(self):
        return iter(self.matriz)

    def resetaLabirinto(self):
        for linha in range(self.qtLinhas):
            for coluna in range(self.qtColunas):
                self.matriz[linha][coluna] = copy.deepcopy(self.celulaPadrao)

    # Corrigido sorteamento de diagonais 
    def SorteiaCelulaVizinha(self, linhaCelulaAtual, colunaCelulaAtual):
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
        vizinhos_validos = []

        for d_linha, d_coluna in direcoes:
            nova_linha = linhaCelulaAtual + d_linha
            nova_coluna = colunaCelulaAtual + d_coluna
            if 0 <= nova_linha < self.qtLinhas and 0 <= nova_coluna < self.qtColunas:
                vizinhos_validos.append((nova_linha, nova_coluna))

        if vizinhos_validos:
            return random.choice(vizinhos_validos)
        else:
            return linhaCelulaAtual, colunaCelulaAtual  # Fallback se não houver vizinhos

    def GeraLabirinto(self):

        self.resetaLabirinto()

        unvisitedCells = self.qtLinhas * self.qtColunas
        currentCellLine, currentCellColumn, neighCellLine, neighCellColumn = -1, -1, -1, -1

        currentCellLine = 0
        currentCellColumn = 0

        self.matriz[0][0].aberta = True
        self.matriz[self.qtLinhas - 1][self.qtColunas - 1].aberta = True
        self.matriz[0][0].visited = True
        self.matriz[self.qtLinhas - 1][self.qtColunas - 1].visited = True
        unvisitedCells -= 2

        while (unvisitedCells > 0):

            # Sorteia um vizinho qualquer da célula atual
            neighCellLine, neighCellColumn = self.SorteiaCelulaVizinha(currentCellLine, currentCellColumn)

            if (self.matriz[neighCellLine][neighCellColumn].visited == False):
                # incluir aqui a rotina paar abrir uma passagem. Por enquanto, apenas pinta a célula
                self.matriz[currentCellLine][currentCellColumn].aberta = True
                self.matriz[neighCellLine][neighCellColumn].visited = True
                '''
                self.matriz[currentCellLine][currentCellColumn].aberta = True
                self.matriz[neighCellLine][neighCellColumn].aberta     = True
                self.matriz[neighCellLine][neighCellColumn].visited    = True
                self.matriz[neighCellLine][neighCellColumn].corPreenchimento = (0, 255, 0)
                '''
                unvisitedCells -= 1
                # cont += 1

            currentCellLine, currentCellColumn = neighCellLine, neighCellColumn

class Malha:
    def __init__(self, qtLinhas, qtColunas, aresta, celulaPadrao):
        self.qtLinhas = qtLinhas
        self.qtColunas = qtColunas
        self.aresta = aresta
        self.celulaPadrao = celulaPadrao
        self.matriz = self.GeraMatriz()

    def __len__(self):
        return len(self.matriz)

    def __iter__(self):
        return iter(self.matriz)

    def __getitem__(self, index):
        return self.matriz[index]

    def __setitem__(self, index, value):
        self.matriz[index] = value

    def __aslist__(self):
        return self.matriz

    def GeraMatriz(self):
        matriz = []
        for i in range(self.qtLinhas):
            linha = []
            for j in range(self.qtColunas):
                #newCell = copy.deepcopy(self.celulaPadrao)
                linha.append(copy.deepcopy(self.celulaPadrao))
            matriz.append(linha)
        return matriz

    def DesenhaLabirinto(self, tela, x, y):
        for linha in range(self.qtLinhas):
            for coluna in range(self.qtColunas):
                self.matriz[linha][coluna].desenhar(tela, x + coluna * self.aresta, y + linha * self.aresta, self.aresta)

def resolve_labirinto(labirinto):
    start = (0, 0)  # Início no canto superior esquerdo
    end = (labirinto.qtLinhas - 1, labirinto.qtColunas - 1)  # Fim no canto inferior direito

    # Função heurística: Distância de Manhattan
    def heuristica(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Definir as direções válidas (cima, baixo, esquerda, direita)
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Estruturas de dados para A*
    open_list = []  # Lista de nós a explorar
    heapq.heappush(open_list, (0 + heuristica(start, end), 0, start))  # (f, g, (x, y))
    came_from = {}  # Para rastrear o caminho
    g_score = {start: 0}  # O custo até cada célula
    f_score = {start: heuristica(start, end)}  # O custo total estimado

    while open_list:
        _, g, current = heapq.heappop(open_list)

        # Se chegarmos ao final, reconstruir o caminho
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            # Marcar as células no caminho
            for (x, y) in path:
                labirinto.matriz[x][y].no_caminho = True
            labirinto.matriz[0][0].no_caminho = True
            return path  # Retorna o caminho

        # Explorar as células vizinhas
        for dx, dy in direcoes:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < labirinto.qtLinhas and 0 <= neighbor[1] < labirinto.qtColunas:
                if labirinto.matriz[neighbor[0]][neighbor[1]].aberta:  # Célula válida
                    tentative_g_score = g + 1  # Custo até o vizinho (a cada movimento)
                    
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        # Melhor caminho encontrado até o vizinho
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristica(neighbor, end)
                        heapq.heappush(open_list, (f_score[neighbor], tentative_g_score, neighbor))

    return None  # Caso não haja caminho

def main():
    pygame.init()

    ### definição das cores
    azul = (50, 50, 255)
    preto = (0, 0, 0)
    branco = (255, 255, 255)
    vermelho = (255, 0, 0)
    verde = (0, 255, 0)
    azul = (0, 0, 255)
    cinza = (128, 128, 128)

    # Dimensões da janela
    [largura, altura] = [600, 300]

    ### Dimensões da malha (matriz NxM)
    N = 20  # número de linhas
    M = 20  # número de colunas
    aresta = 10  # dimensão dos lados das células

    # cores: preenchimento - visitada - linha - aberta
    celulaPadrao = Celula(ArestasFechadas(False, False, False, False), vermelho, cinza, preto, azul, False, False)
    labirinto = AldousBroder(N, M, aresta, celulaPadrao)
    labirinto.GeraLabirinto()
    tem_resolucao = resolve_labirinto(labirinto)

    # Cria a janela
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Mostra Malha')

    ### Criação da fonte para o texto
    fonte = pygame.font.SysFont("Arial", 32)  # Defina o tamanho da fonte (32 é só um exemplo)
    texto = fonte.render("Labirinto sem Solução", True, (255, 165, 0))  # Preto para o texto

    ###
    ### Loop principal
    ###
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ### preenche a tela com a cor branca
        tela.fill(branco)

        ### centraliza a grade na janela
        [linha, coluna] = ((tela.get_width() - (M * aresta)) // 2,
                           (tela.get_height() - (N * aresta)) // 2)
        # desenhar_grade(tela, linha, coluna, aresta, N, M, matriz)
        labirinto.matriz.DesenhaLabirinto(tela, linha, coluna)

        ### centraliza o texto na tela
        texto_rect = texto.get_rect(center=(largura // 2, altura // 2))  # Centraliza o texto
        if not tem_resolucao:
            tela.blit(texto, texto_rect)  # Desenha o texto na tela

        ### atualiza a tela
        pygame.display.flip()

if __name__ == '__main__':
    main()