import socket
import threading

class JogoDotsAndBoxes:
    def __init__(self):
        self.jogadores = []
        self.tamanho = 5  # Definindo o tamanho do tabuleiro
        self.tabuleiro = [[' ' for _ in range(self.tamanho)] for _ in range(self.tamanho)]

    def adicionar_jogador(self, jogador):
        if len(self.jogadores) < 2:
            self.jogadores.append(jogador)
            return True
        return False

    def jogar(self, linha, coluna, jogador):
        # Verifica se a linha e a coluna estão dentro dos limites
        if 0 <= linha < self.tamanho and 0 <= coluna < self.tamanho:
            if self.tabuleiro[linha][coluna] == ' ':
                self.tabuleiro[linha][coluna] = jogador
                return True
            else:
                print("Posição já ocupada.")
                return False
        else:
            print("Movimento fora dos limites!")
            return False

    def verificar_vencedor(self):
        # Lógica para verificar se o jogo acabou ou se há um vencedor
        return None

class Servidor:
    def __init__(self, host="localhost", porta=5555):
        self.host = host
        self.porta = porta
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.jogos = {}
        self.fila_espera = []
    
    def iniciar(self):
        self.servidor.bind((self.host, self.porta))
        self.servidor.listen(5)
        print(f"Servidor iniciado em {self.host}:{self.porta}")

        while True:
            cliente, endereco = self.servidor.accept()
            print(f"Nova conexão de {endereco}")
            thread_cliente = threading.Thread(target=self.tratar_cliente, args=(cliente,))
            thread_cliente.start()

    def tratar_cliente(self, cliente):
        jogador = cliente.recv(1024).decode()  # Recebe nome do jogador
        print(f"Jogador {jogador} conectado.")

        if len(self.fila_espera) == 0:
            self.fila_espera.append((cliente, jogador))
            cliente.send("Aguardando outro jogador...".encode())
        else:
            oponente_cliente, oponente_nome = self.fila_espera.pop(0)
            jogo = JogoDotsAndBoxes()
            jogo.adicionar_jogador(jogador)
            jogo.adicionar_jogador(oponente_nome)

            self.jogos[jogador] = jogo
            self.jogos[oponente_nome] = jogo

            oponente_cliente.send("Iniciando partida...".encode())
            cliente.send("Iniciando partida...".encode())
            threading.Thread(target=self.partida, args=(cliente, oponente_cliente, jogo)).start()

    def partida(self, cliente1, cliente2, jogo):
        while True:
            # Jogador 1 faz sua jogada
            cliente1.send("Sua vez: Faça um movimento no formato linha,coluna".encode())
            movimento = cliente1.recv(1024).decode()
            linha, coluna = map(int, movimento.split(','))
    
            if jogo.jogar(linha, coluna, 'X'):
                cliente2.send(f"O jogador {jogo.jogadores[0]} jogou na posição {linha},{coluna}".encode())
                cliente1.send("Movimento realizado com sucesso.".encode())
                # Aqui você pode adicionar lógica para verificar se o jogo acabou
            else:
                cliente1.send("Movimento inválido! Tente novamente.".encode())
                continue  # Retorna para o começo do loop para que o jogador tente novamente
    
            # Jogador 2 faz sua jogada
            cliente2.send("Sua vez: Faça um movimento no formato linha,coluna".encode())
            movimento = cliente2.recv(1024).decode()
            linha, coluna = map(int, movimento.split(','))
    
            if jogo.jogar(linha, coluna, 'O'):
                cliente1.send(f"O jogador {jogo.jogadores[1]} jogou na posição {linha},{coluna}".encode())
                cliente2.send("Movimento realizado com sucesso.".encode())
                # Aqui você pode adicionar lógica para verificar se o jogo acabou
            else:
                cliente2.send("Movimento inválido! Tente novamente.".encode())
                continue  # Retorna para o começo do loop para que o jogador tente novamente

# Inicializando o servidor
if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciar()
