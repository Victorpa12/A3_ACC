from sys import argv
from time import sleep
#from tabuleiro import Tabuleiro
import socket

X_TAB = 5
Y_TAB = 4

SERVER_HOST = "localhost"
SERVER_PORT = 1234

BUFFER_SIZE = 1024

# armazena os jogadores que estão esperando por uma partida
fila_espera = []

def trata_mensagem(data, addr):

    msg = data.decode()
    dados = msg.split(':')

    cod = int(dados[0])
    nome = dados[1]

    print(msg)
    print(dados)
    print(cod)
    print(nome)

    match cod:
        case 1:
            fila_espera.append({
                'nome': nome
            })
        case "_":
            print("Não entendi a msg!")
            

def main(args):

    # configura uma conexão socket UDP/IPv4
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as skt:
        skt.bind((SERVER_HOST, SERVER_PORT))
        
        while True:

            num_jogadores = len(fila_espera)

            print(f"A fila de espera possui {num_jogadores} jogadores")
            print("Aguardando conexão de jogadores ...")

            data, addr = skt.recvfrom(BUFFER_SIZE)
            if(data):
                trata_mensagem(data, addr)

if __name__ == '__main__':
    main(argv)