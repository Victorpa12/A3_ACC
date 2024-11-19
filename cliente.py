import pygame
import socket
import pickle

# Defina a tela e as cores
SCREEN = WIDTH, HEIGHT = 300, 300
CELLSIZE = 40
PADDING = 20
ROWS = COLS = 5  # Ajuste para o tamanho 5x5
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
GREEN = (0, 255, 0)
BLACK = (12, 12, 12)

font = pygame.font.SysFont('cursive', 25)

class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.index = self.r * 5 + self.c
        self.rect = pygame.Rect((self.c * CELLSIZE + 2 * PADDING, self.r * CELLSIZE + 3 * PADDING, CELLSIZE, CELLSIZE))
        self.sides = [False, False, False, False]
        self.winner = None

    def update(self, win):
        if self.winner:
            pygame.draw.rect(win, self.color, self.rect)
            win.blit(self.text, (self.rect.centerx - 5, self.rect.centery - 7))

        for index, side in enumerate(self.sides):
            if side:
                pygame.draw.line(win, WHITE, (self.rect.topleft), (self.rect.bottomright), 2)

def create_cells():
    cells = []
    for r in range(5):
        for c in range(5):
            cells.append(Cell(r, c))
    return cells

# Função para conectar ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 65432))

def receive_game_state():
    """Recebe o estado atualizado do jogo do servidor"""
    data = client.recv(4096)
    game_state = pickle.loads(data)
    return game_state

# Loop do cliente
cells = create_cells()
running = True
while running:
    win.fill(BLACK)

    # Recebe o estado do jogo do servidor
    game_state = receive_game_state()
    cells = game_state['cells']
    turn = game_state['turn']
    player_id = game_state['player_id']

    # Exibição do estado no Pygame
    for cell in cells:
        cell.update(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            # Lógica de jogada (clique nas células)
            for cell in cells:
                if cell.rect.collidepoint(pos):
                    # Envia a jogada para o servidor
                    move = {"index": cell.index, "direction": "right"}  # Exemplo de direções
                    client.send(pickle.dumps(move))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    pygame.display.update()

client.close()
pygame.quit()
