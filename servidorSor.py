from sys import argv
from time import sleep
import socket

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
            
num_jogadores = 0

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

            if num_jogadores >= 2:
                print("Iniciando partida ...")
                sleep(5)
                print("Partida iniciada!")
                num_jogadores = 0

if __name__ == '__main__':
    main(argv)
