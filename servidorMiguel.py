from sys import argv
import socket
import pygame
from time import sleep

SCREEN = WIDTH, HEIGHT = 300, 300  # Dimensões da tela
CELLSIZE = 40  # Tamanho de cada célula
PADDING = 20  # Espaçamento
# Cores
WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
GREEN = (0, 255, 0)
BLACK = (12, 12, 12)
ROWS = COLS = (WIDTH - 4 * PADDING) // CELLSIZE  # Número de linhas e colunas


font = pygame.font.SysFont('cursive', 25)  # Define a fonte

HOST = '127.0.0.1'
PORT = 4000
BUFFER_SIZE = 1024
fila_espera = []

def trata_mensagem(data, addr):

    msg = data.decode()
    dados = msg.split(':')
    cod = int(dados[0])
    
    
    match cod:
        case 1:
            nome = dados[1]
            fila_espera.append(f"{len(fila_espera)+1}: {nome} : {addr}")
        
        case 2:
            quit = bool(dados[1])
            reset = bool(dados[2])
            pos = dados[3]
            up = bool(dados[4])
            right = bool(dados[5])
            bottom = bool(dados[6])
            left = bool(dados[7])
            
            
        case "_":
            print("Não entendi a msg!")

    print(dados)
    print(fila_espera)

def playerAddr (index):
    playerData = fila_espera[index].split(':')
    paddr = playerData[2]
    addr9 = paddr.split("('")
    addr0 = addr9[1].split(')')
    playeraddr = addr0[0].split("',")
    addr = (playeraddr[0], int(playeraddr[1]))
    print(addr)
    return addr

def playerName (index):
    playerData = fila_espera[index].split(':')
    nome = playerData[1]
    return nome



            
num_jogadores = 0

def main(args):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        
        party = 1
        while True:
            num_jogadores = len(fila_espera)
            print(f"Servidor UDP iniciado. Aguardando dados em {HOST}:{PORT}...")
            
            
            print(f"A fila de espera possui {num_jogadores} jogadores")
            print("Aguardando conexão de jogadores ...")

            data, addr = s.recvfrom(BUFFER_SIZE)
            print(f"Conexão recebida de {addr}")
            
            if(data):
                
                trata_mensagem(data, addr)
                
            if len(fila_espera) == 2:
                res = f":A partida {party} vai começar"
                
                print("Iniciando partida ...")
                sleep(3)
                print("Partida iniciada!")
                s.sendto(res.encode(), playerAddr(0))
                s.sendto(res.encode(), playerAddr(1))
                fila_espera.clear()
                party += 1




                
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

                

if __name__ == '__main__':
    main(argv)
    
    

