import socket
import pygame

HOST = '127.0.0.1'
PORT = 4000

SCREEN = WIDTH, HEIGHT = 300, 300  # Dimensões da tela
CELLSIZE = 40  # Tamanho de cada célula
PADDING = 20  # Espaçamento
ROWS = COLS = (WIDTH - 4 * PADDING) // CELLSIZE  # Número de linhas e colunas

WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
GREEN = (0, 255, 0)
BLACK = (12, 12, 12)


def trata_mensagem():
    msgsrv = data.decode()
    dados = msgsrv.split(':')
    cod = int(dados[0])
    
    
    match cod:
        case 1:
            partida = dados[1]
            print(partida)
            main()
        case 2:
            jogada()
        case "_":
            print("Não entendi a msg!")





def update(self, win):
            if self.winner:  # Se a célula tem um vencedor
                pygame.draw.rect(win, self.color, self.rect)  # Desenha o retângulo da célula
                win.blit(self.text, (self.rect.centerx - 5, self.rect.centery - 7))  # Desenha o texto do vencedor
            for index, side in enumerate(self.sides):  # Para cada lado da célula
                if side:  # Se o lado foi desenhado
                    pygame.draw.line(win, WHITE, self.edges[index][0], self.edges[index][1], 2)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#msg =(f"1:{input('Digite seu nome: ')}")
#player =  (f"1:{input('player(1, 2): ')}")
msg = "1:João"
player = "1"
s.sendto(msg.encode(), (HOST, PORT))
data = s.recv(1024)
if data:
    trata_mensagem()
else:
    print("Aguardando oponente...")

    
def main():
    pygame.init()  # Inicializa o pygame
    win = pygame.display.set_mode([WIDTH, HEIGHT])  # Cria a janela do jogo
    pygame.display.set_caption("Dots And Boxes")  # Define o título da janela

    running = True  # Flag para controlar o loop principal
    while running:
    
        for event in pygame.event.get():  # Para cada evento
            if event.type == pygame.QUIT:  # Se o evento é para sair
                quit = True  # Define a flag de saída

            if event.type == pygame.MOUSEBUTTONDOWN:  # Se o botão do mouse foi pressionado
                pos = event.pos  # Posição do clique

            if event.type == pygame.MOUSEBUTTONUP:  # Se o botão do mouse foi solto
                pos = None  # Reseta a posição após soltar o mouse

            if event.type == pygame.KEYDOWN:  # Se uma tecla foi pressionada
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:  # Se a tecla é 'q' ou 'ESC'
                    quit = True
                if event.key == pygame.K_r:  # Se a tecla é 'r'
                    reset = True  # Define a flag de reset
                    
                
                if event.key == pygame.K_UP: up = True  # Se a tecla é 'UP'
                if event.key == pygame.K_RIGHT: right = True  # Se a tecla é 'RIGHT'
                if event.key == pygame.K_DOWN: bottom = True  # Se a tecla é 'DOWN'
                if event.key == pygame.K_LEFT: left = True  # Se a tecla é 'LEFT'

            if event.type == pygame.KEYUP:  # Se uma tecla foi solta
                if event.key == pygame.K_UP: up = False  # Reseta a direção 'UP'
                if event.key == pygame.K_RIGHT: right = False  # Reseta a direção 'RIGHT'
                if event.key == pygame.K_DOWN: bottom = False  # Reseta a direção 'DOWN'
                if event.key == pygame.K_LEFT: left = False  # Reseta a direção 'LEFT'
        s.sendto(str.encode(f'2:{quit}:{reset}:{pos}:{up}:{right}:{bottom}:{left}'), (HOST, PORT))
            # Desenha o tabuleiro
        for r in range(ROWS + 1):
            for c in range(COLS + 1):
                pygame.draw.circle(win, WHITE, (c * CELLSIZE + 2 * PADDING, r * CELLSIZE + 3 * PADDING), 2)  # Desenha os pontos do tabuleiro

        # Atualiza células e verifica cliques
        for cell in cells:
            cell.update(win)  # Atualiza a célula
            if pos and cell.rect.collidepoint(pos):  # Se houve um clique e ele está dentro da célula
                ccell = cell  # Define a célula clicada
                




