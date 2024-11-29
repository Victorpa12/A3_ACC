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
                res = f"2:A partida {party} vai começar"
                
                print("Iniciando partida ...")
                sleep(3)
                print("Partida iniciada!")
                s.sendto(res.encode(), playerAddr(0))
                s.sendto(res.encode(), playerAddr(1))
                fila_espera.clear()
                party += 1

                
                

                

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
    
    

