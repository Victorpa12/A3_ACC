
import pygame

# Configurações iniciais
SCREEN = WIDTH, HEIGHT = 300, 300  # Dimensões da tela
CELLSIZE = 40  # Tamanho de cada célula
PADDING = 20  # Espaçamento
ROWS = COLS = (WIDTH - 4 * PADDING) // CELLSIZE  # Número de linhas e colunas

pygame.init()  # Inicializa o pygame
win = pygame.display.set_mode([WIDTH, HEIGHT])  # Cria a janela do jogo

# Cores
WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
GREEN = (0, 255, 0)
BLACK = (12, 12, 12)

# Fonte
font = pygame.font.SysFont('cursive', 25)  # Define a fonte

# Classe para representar cada célula
class Cell:
    def __init__(self, r, c):
        self.r = r  # Linha da célula
        self.c = c  # Coluna da célula
        self.index = self.r * ROWS + self.c  # Índice único da célula
        self.rect = pygame.Rect((self.c * CELLSIZE + 2 * PADDING, 
                                 self.r * CELLSIZE + 3 * PADDING, 
                                 CELLSIZE, CELLSIZE))  # Retângulo que representa a célula
        self.edges = [  # Coordenadas das bordas da célula
            [(self.rect.left, self.rect.top), (self.rect.right, self.rect.top)],
            [(self.rect.right, self.rect.top), (self.rect.right, self.rect.bottom)],
            [(self.rect.right, self.rect.bottom), (self.rect.left, self.rect.bottom)],
            [(self.rect.left, self.rect.bottom), (self.rect.left, self.rect.top)]
        ]
        self.sides = [False, False, False, False]  # Lados da célula (se foram desenhados ou não)
        self.winner = None  # Vencedor da célula (se todos os lados foram desenhados)

    def checkwin(self, winner):
        if not self.winner:  # Se a célula ainda não tem um vencedor
            if self.sides == [True] * 4:  # Se todos os lados foram desenhados
                self.winner = winner  # Define o vencedor
                self.color = GREEN if winner == 'X' else RED  # Define a cor com base no vencedor
                self.text = font.render(self.winner, True, WHITE)  # Renderiza o texto do vencedor
                return 1  # Retorna 1 indicando que a célula foi preenchida
        return 0  # Retorna 0 se a célula não foi preenchida

    def update(self, win):
        if self.winner:  # Se a célula tem um vencedor
            pygame.draw.rect(win, self.color, self.rect)  # Desenha o retângulo da célula
            win.blit(self.text, (self.rect.centerx - 5, self.rect.centery - 7))  # Desenha o texto do vencedor
        for index, side in enumerate(self.sides):  # Para cada lado da célula
            if side:  # Se o lado foi desenhado
                pygame.draw.line(win, WHITE, self.edges[index][0], self.edges[index][1], 2)  # Desenha a linha do lado

# Funções auxiliares
def create_cells():
    return [Cell(r, c) for r in range(ROWS) for c in range(COLS)]  # Cria uma lista de células

def reset_game():
    cells = create_cells()  # Cria as células
    fillcount = 0  # Contador de células preenchidas
    p1_score = 0  # Pontuação do jogador 1
    p2_score = 0  # Pontuação do jogador 2
    players = ['X', 'O']  # Lista de jogadores
    turn = 0  # Turno atual
    player = players[turn]  # Jogador atual
    next_turn = False  # Indica se é o próximo turno
    return cells, fillcount, p1_score, p2_score, players, turn, player, next_turn  # Retorna as variáveis do jogo

# Variáveis do jogo
gameover = False  # Indica se o jogo acabou
cells, fillcount, p1_score, p2_score, players, turn, player, next_turn = reset_game()  # Inicializa as variáveis do jogo
pos, ccell = None, None  # Posição do clique e célula clicada
up, right, bottom, left = False, False, False, False  # Direções das teclas pressionadas

# Loop principal
running = True
while running:
    
    win.fill(BLACK)  # Preenche a tela com a cor preta
    for event in pygame.event.get():  # Para cada evento
        if event.type == pygame.QUIT:  # Se o evento é para sair
            running = False  # Encerra o loop

        if event.type == pygame.MOUSEBUTTONDOWN:  # Se o botão do mouse foi pressionado
            pos = event.pos  # Posição do clique

        if event.type == pygame.MOUSEBUTTONUP:  # Se o botão do mouse foi solto
            pos = None  # Reseta a posição após soltar o mouse

        if event.type == pygame.KEYDOWN:  # Se uma tecla foi pressionada
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:  # Se a tecla é 'q' ou 'ESC'
                running = False  # Encerra o loop
            if event.key == pygame.K_r:  # Se a tecla é 'r'
                gameover = False  # Reseta o estado de fim de jogo
                cells, fillcount, p1_score, p2_score, players, turn, player, next_turn = reset_game()  # Reseta o jogo
            if not gameover:  # Se o jogo não acabou
                if event.key == pygame.K_UP: up = True  # Se a tecla é 'UP'
                if event.key == pygame.K_RIGHT: right = True  # Se a tecla é 'RIGHT'
                if event.key == pygame.K_DOWN: bottom = True  # Se a tecla é 'DOWN'
                if event.key == pygame.K_LEFT: left = True  # Se a tecla é 'LEFT'

        if event.type == pygame.KEYUP:  # Se uma tecla foi solta
            if event.key == pygame.K_UP: up = False  # Reseta a direção 'UP'
            if event.key == pygame.K_RIGHT: right = False  # Reseta a direção 'RIGHT'
            if event.key == pygame.K_DOWN: bottom = False  # Reseta a direção 'DOWN'
            if event.key == pygame.K_LEFT: left = False  # Reseta a direção 'LEFT'

    # Desenha o tabuleiro
    for r in range(ROWS + 1):
        for c in range(COLS + 1):
            pygame.draw.circle(win, WHITE, (c * CELLSIZE + 2 * PADDING, r * CELLSIZE + 3 * PADDING), 2)  # Desenha os pontos do tabuleiro

    # Atualiza células e verifica cliques
    for cell in cells:
        cell.update(win)  # Atualiza a célula
        if pos and cell.rect.collidepoint(pos):  # Se houve um clique e ele está dentro da célula
            ccell = cell  # Define a célula clicada
        

    # Lógica para atualização de estados
    if ccell:
        index = ccell.index  # Índice da célula clicada
        if not ccell.winner:  # Se a célula não tem um vencedor
            pygame.draw.circle(win, RED, (ccell.rect.centerx, ccell.rect.centery), 2)  # Desenha um círculo vermelho no centro da célula
        if up and not ccell.sides[0]:  # Se a direção 'UP' foi pressionada e o lado superior não foi desenhado
            ccell.sides[0] = True  # Desenha o lado superior
            if index - ROWS >= 0:  # Se a célula acima existe
                cells[index - ROWS].sides[2] = True  # Desenha o lado inferior da célula acima
            next_turn = True  # Indica que é o próximo turno
        if right and not ccell.sides[1]:  # Se a direção 'RIGHT' foi pressionada e o lado direito não foi desenhado
            ccell.sides[1] = True  # Desenha o lado direito
            if (index + 1) % COLS > 0:  # Se a célula à direita existe
                cells[index + 1].sides[3] = True  # Desenha o lado esquerdo da célula à direita
            next_turn = True  # Indica que é o próximo turno
        if bottom and not ccell.sides[2]:  # Se a direção 'DOWN' foi pressionada e o lado inferior não foi desenhado
            ccell.sides[2] = True  # Desenha o lado inferior
            if index + ROWS < len(cells):  # Se a célula abaixo existe
                cells[index + ROWS].sides[0] = True  # Desenha o lado superior da célula abaixo
            next_turn = True  # Indica que é o próximo turno
        if left and not ccell.sides[3]:  # Se a direção 'LEFT' foi pressionada e o lado esquerdo não foi desenhado
            ccell.sides[3] = True  # Desenha o lado esquerdo
            if index % COLS > 0:  # Se a célula à esquerda existe
                cells[index - 1].sides[1] = True  # Desenha o lado direito da célula à esquerda
            next_turn = True  # Indica que é o próximo turno
       
        points_this_turn = 0
        # Verifica se a célula atual ou as células adjacentes foram preenchidas
        res = ccell.checkwin(player) # Verifica se a célula foi preenchida
        if index - ROWS >= 0:  # Se a célula acima existe
            res += cells[index - ROWS].checkwin(player)  # Verifica se a célula acima foi preenchida
        if (index + 1) % COLS > 0:  # Se a célula à direita existe
            res += cells[index + 1].checkwin(player)  # Verifica se a célula à direita foi preenchida
        if index + ROWS < len(cells):  # Se a célula abaixo existe
            res += cells[index + ROWS].checkwin(player)  # Verifica se a célula abaixo foi preenchida
        if index % COLS > 0:  # Se a célula à esquerda existe
            res += cells[index - 1].checkwin(player)  # Verifica se a célula à esquerda foi preenchida

            # Após fechar os lados, verifique se a célula foi fechada e conte os pontos
        for cell in cells:
            points = cell.checkwin(player)
            points_this_turn += points  # Acumula os pontos para este turno
            
        if res:  # Se alguma célula foi preenchida
            fillcount += res  # Incrementa o contador de células preenchidas
            if player == 'X': p1_score += res  # Incrementa a pontuação do jogador 1
            else: p2_score += res  # Incrementa a pontuação do jogador 2
            if fillcount == ROWS * COLS:  # Se todas as células foram preenchidas
                gameover = True  # Indica que o jogo acabou
        
        if next_turn and not res:  # Se é o próximo turno e nenhuma célula foi preenchida
            turn = (turn + 1) % len(players)  # Alterna o turno
            player = players[turn]  # Alterna o jogador
            next_turn = False  # Reseta a indicação de próximo turno
        

    # Mostra pontuação
    p1img = font.render(f'Jogador 1: {p1_score}', True, BLUE)  # Renderiza a pontuação do jogador 1
    p2img = font.render(f'Jogador 2: {p2_score}', True, BLUE)  # Renderiza a pontuação do jogador 2
    win.blit(p1img, (2 * PADDING, 15))  # Desenha a pontuação do jogador 1 na tela
    win.blit(p2img, (WIDTH - 2 * PADDING - p2img.get_width(), 15))  # Desenha a pontuação do jogador 2 na tela

    # Indicador de jogador
    if player == 'X':
        pygame.draw.line(win, BLUE, (2 * PADDING, 40), (2 * PADDING + p1img.get_width(), 40), 2)  # Desenha a linha indicadora do jogador 1
    else:
        pygame.draw.line(win, BLUE, (WIDTH - 2 * PADDING - p2img.get_width(), 40), (WIDTH - 2 * PADDING, 40), 2)  # Desenha a linha indicadora do jogador 2

    # Exibe mensagem de fim de jogo
    if gameover:
        rect = pygame.Rect(30, 76, WIDTH - 70, HEIGHT - 150)  # Define o retângulo da mensagem de fim de jogo
        pygame.draw.rect(win, BLACK, rect)  # Desenha o retângulo da mensagem
        pygame.draw.rect(win, WHITE, rect, 2)  # Desenha a borda do retângulo

        over = font.render('Fim de Jogo', True, WHITE)  # Renderiza o texto "Fim de Jogo"
        winner = '1' if p1_score > p2_score else '2'  # Define o vencedor
        winner_img = font.render(f'Jogador {winner} venceu!', True, GREEN)  # Renderiza o texto do vencedor

        msg_restart = font.render('Pressione R para reiniciar', True, RED)  # Renderiza a mensagem de reinício
        msg_exit = font.render('Pressione ESC para sair', True, RED)  # Renderiza a mensagem de saída

        # Centraliza e exibe as mensagens no retângulo
        win.blit(over, (rect.centerx - over.get_width() // 2, rect.y + 20))  # "Fim de Jogo"
        win.blit(winner_img, (rect.centerx - winner_img.get_width() // 2, rect.centery - 40))  # "Jogador X venceu!"
        win.blit(msg_restart, (rect.centerx - msg_restart.get_width() // 2, rect.centery + 10))  # "Pressione R para reiniciar"
        win.blit(msg_exit, (rect.centerx - msg_exit.get_width() // 2, rect.centery + 40))  # "Pressione ESC para sair"

    pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 2)  # Desenha a borda da tela
    pygame.display.update()  # Atualiza a tela