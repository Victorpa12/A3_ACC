
import pygame

# Configurações iniciais
SCREEN = WIDTH, HEIGHT = 300, 300
CELLSIZE = 40
PADDING = 20
ROWS = COLS = (WIDTH - 4 * PADDING) // CELLSIZE

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

# Cores
WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
GREEN = (0, 255, 0)
BLACK = (12, 12, 12)

# Fonte
font = pygame.font.SysFont('cursive', 25)

# Classe para representar cada célula
class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.index = self.r * ROWS + self.c
        self.rect = pygame.Rect((self.c * CELLSIZE + 2 * PADDING, 
                                 self.r * CELLSIZE + 3 * PADDING, 
                                 CELLSIZE, CELLSIZE))
        self.edges = [
            [(self.rect.left, self.rect.top), (self.rect.right, self.rect.top)],
            [(self.rect.right, self.rect.top), (self.rect.right, self.rect.bottom)],
            [(self.rect.right, self.rect.bottom), (self.rect.left, self.rect.bottom)],
            [(self.rect.left, self.rect.bottom), (self.rect.left, self.rect.top)]
        ]
        self.sides = [False, False, False, False]
        self.winner = None

    def checkwin(self, winner):
        if not self.winner:
            if self.sides == [True] * 4:
                self.winner = winner
                self.color = GREEN if winner == 'X' else RED
                self.text = font.render(self.winner, True, WHITE)
                return 1
        return 0

    def update(self, win):
        if self.winner:
            pygame.draw.rect(win, self.color, self.rect)
            win.blit(self.text, (self.rect.centerx - 5, self.rect.centery - 7))
        for index, side in enumerate(self.sides):
            if side:
                pygame.draw.line(win, WHITE, self.edges[index][0], self.edges[index][1], 2)

# Funções auxiliares
def create_cells():
    return [Cell(r, c) for r in range(ROWS) for c in range(COLS)]

def reset_game():
    cells = create_cells()
    fillcount = 0
    p1_score = 0
    p2_score = 0
    players = ['X', 'O']
    turn = 0
    player = players[turn]
    next_turn = False
    return cells, fillcount, p1_score, p2_score, players, turn, player, next_turn

# Variáveis do jogo
gameover = False
cells, fillcount, p1_score, p2_score, players, turn, player, next_turn = reset_game()
pos, ccell = None, None
up, right, bottom, left = False, False, False, False

# Loop principal
running = True
while running:
    win.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos  # Posição do clique

        if event.type == pygame.MOUSEBUTTONUP:
            pos = None  # Reseta a posição após soltar o mouse

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_r:
                gameover = False
                cells, fillcount, p1_score, p2_score, players, turn, player, next_turn = reset_game()
            if not gameover:
                if event.key == pygame.K_UP: up = True
                if event.key == pygame.K_RIGHT: right = True
                if event.key == pygame.K_DOWN: bottom = True
                if event.key == pygame.K_LEFT: left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: up = False
            if event.key == pygame.K_RIGHT: right = False
            if event.key == pygame.K_DOWN: bottom = False
            if event.key == pygame.K_LEFT: left = False

    # Desenha o tabuleiro
    for r in range(ROWS + 1):
        for c in range(COLS + 1):
            pygame.draw.circle(win, WHITE, (c * CELLSIZE + 2 * PADDING, r * CELLSIZE + 3 * PADDING), 2)

    # Atualiza células e verifica cliques
    for cell in cells:
        cell.update(win)
        if pos and cell.rect.collidepoint(pos):
            ccell = cell

    # Lógica para atualização de estados
    if ccell:
        index = ccell.index
        if not ccell.winner:
            pygame.draw.circle(win, RED, (ccell.rect.centerx, ccell.rect.centery), 2)
        if up and not ccell.sides[0]:
            ccell.sides[0] = True
            if index - ROWS >= 0:
                cells[index - ROWS].sides[2] = True
            next_turn = True
        if right and not ccell.sides[1]:
            ccell.sides[1] = True
            if (index + 1) % COLS > 0:
                cells[index + 1].sides[3] = True
            next_turn = True
        if bottom and not ccell.sides[2]:
            ccell.sides[2] = True
            if index + ROWS < len(cells):
                cells[index + ROWS].sides[0] = True
            next_turn = True
        if left and not ccell.sides[3]:
            ccell.sides[3] = True
            if index % COLS > 0:
                cells[index - 1].sides[1] = True
            next_turn = True
        res = ccell.checkwin(player)
        if res:
            fillcount += res
            if player == 'X': p1_score += 1
            else: p2_score += 1
            if fillcount == ROWS * COLS:
                gameover = True
        if next_turn:
            turn = (turn + 1) % len(players)
            player = players[turn]
            next_turn = False

    # Mostra pontuação
    p1img = font.render(f'Jogador 1: {p1_score}', True, BLUE)
    p2img = font.render(f'Jogador 2: {p2_score}', True, BLUE)
    win.blit(p1img, (2 * PADDING, 15))
    win.blit(p2img, (WIDTH - 2 * PADDING - p2img.get_width(), 15))

    # Indicador de jogador
    if player == 'X':
        pygame.draw.line(win, BLUE, (2 * PADDING, 40), (2 * PADDING + p1img.get_width(), 40), 2)
    else:
        pygame.draw.line(win, BLUE, (WIDTH - 2 * PADDING - p2img.get_width(), 40), (WIDTH - 2 * PADDING, 40), 2)

    # Exibe mensagem de fim de jogo
    if gameover:
        rect = pygame.Rect(50, 100, WIDTH - 100, HEIGHT - 200)
        pygame.draw.rect(win, BLACK, rect)
        pygame.draw.rect(win, RED, rect, 2)
        over = font.render('Fim de Jogo', True, WHITE)
        winner = '1' if p1_score > p2_score else '2'
        winner_img = font.render(f'Jogador {winner} venceu!', True, GREEN)
        msg = font.render('Pressione R para reiniciar', True, RED)
        win.blit(over, (rect.centerx - over.get_width() // 2, rect.y + 20))
        win.blit(winner_img, (rect.centerx - winner_img.get_width() // 2, rect.centery - 20))
        win.blit(msg, (rect.centerx - msg.get_width() // 2, rect.bottom - 40))

    pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 2)
    pygame.display.update()