import socket
import pickle
import pygame

# Definições de rede
HOST = '127.0.0.1'
PORT = 65432

# Inicializa o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Servidor iniciado. Aguardando conexão em {HOST}:{PORT}...")
conn, addr = server.accept()
print(f"Conexão recebida de {addr}")

# Defina as classes do jogo, como 'Cell', etc.
class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.index = self.r * 5 + self.c  # 5 linhas e colunas no exemplo
        self.rect = pygame.Rect((self.c*40 + 20, self.r*40 + 20, 40, 40))
        self.sides = [False, False, False, False]  # Cima, direita, baixo, esquerda
        self.winner = None
        self.color = (0, 0, 0)
        self.text = None

    def checkwin(self, winner):
        if all(self.sides) and not self.winner:
            self.winner = winner
            self.color = (0, 255, 0) if winner == 'X' else (255, 0, 0)
            return 1
        return 0

    def update(self, win):
        if self.winner:
            pygame.draw.rect(win, self.color, self.rect)
            win.blit(self.text, (self.rect.centerx-5, self.rect.centery-7))

        for index, side in enumerate(self.sides):
            if side:
                pygame.draw.line(win, (255, 255, 255), (self.rect.topleft), (self.rect.bottomright), 2)

def create_cells():
    cells = []
    for r in range(5):
        for c in range(5):
            cells.append(Cell(r, c))
    return cells

# Estado inicial do jogo
cells = create_cells()
turn = 0
players = ['X', 'O']

def send_game_state():
    """Envia o estado do jogo para o cliente"""
    game_state = {
        "cells": cells,
        "turn": turn,
        "player_id": players[turn]
    }
    conn.send(pickle.dumps(game_state))

while True:
    data = conn.recv(4096)
    if data:
        move = pickle.loads(data)  # Recebe a jogada
        index = move["index"]
        direction = move["direction"]

        # Atualiza a jogada no jogo (marcando o lado da célula)
        cell = cells[index]
        if direction == "up":
            cell.sides[0] = True
        elif direction == "right":
            cell.sides[1] = True
        elif direction == "down":
            cell.sides[2] = True
        elif direction == "left":
            cell.sides[3] = True

        # Alterna o turno
        turn = (turn + 1) % 2

        # Envia o estado do jogo para o cliente
        send_game_state()
