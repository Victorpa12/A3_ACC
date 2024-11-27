from sys import argv
import socket
from time import sleep
from DotsAndBoxes import dotsandboxes

HOST = '127.0.0.1'
PORT = 4000
BUFFER_SIZE = 1024
fila_espera = []

def trata_mensagem(data, addr):

    msg = data.decode()
    dados = msg.split(':')

    cod = int(dados[0])
    nome = dados[1]
    
    match cod:
        case 1:
            
            fila_espera.append(f"{len(fila_espera)+1}: {nome} : {addr}")
            
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
        

        while True:
            num_jogadores = len(fila_espera)+1
            print(f"Servidor UDP iniciado. Aguardando dados em {HOST}:{PORT}...")
            
            
            print(f"A fila de espera possui {num_jogadores} jogadores")
            print("Aguardando conexão de jogadores ...")

            data, addr = s.recvfrom(BUFFER_SIZE)
            print(f"Conexão recebida de {addr}")
            
            if(data):
                trata_mensagem(data, addr)
                playerAddr(0)
                res = "sua partida vai começar"
            if num_jogadores >= 2:
                print("Iniciando partida ...")
                sleep(5)
                print("Partida iniciada!")
                s.sendto(res.encode(), playerAddr(0))
                s.sendto(res.encode(), playerAddr(1))
                dotsandboxes()
                fila_espera.clear()

                
                

                

# while True:
#     # data = conn.recv(1024)
#     # decData = data.decode()
#     # dados = decData.split(':')

#     # i = int(dados[0])
#     # msg = dados[1]
#     i = 0
#     if i > 10:
#         break

if __name__ == '__main__':
    main(argv)
    
    

