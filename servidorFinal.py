from sys import argv
import socket
from time import sleep

HOST = '127.0.0.1'
PORT = 4000
BUFFER_SIZE = 1024
fila_espera = []
send = ""
party = 1
def trata_mensagem(data, addr):

    msg = data.decode()
    dados = msg.split(':')
    cod = int(dados[0])
    # Converte a string para booleano
    def convertbool(dados):
        if dados == 'True':
            real_bool = True
        elif dados == 'False':
            real_bool = False
        else:
            raise ValueError("A string deve ser 'True' ou 'False'")
        return real_bool


    
    match cod:
        case 1:
            nome = dados[1]
            fila_espera.append(f"{len(fila_espera)+1}: {nome} : {addr}")
        
        case 2:
            quit = convertbool(dados[1])
            reset = convertbool(dados[2])
            pos = dados[3]
            up = convertbool(dados[4])
            right = convertbool(dados[5])
            bottom = convertbool(dados[6])
            left = convertbool(dados[7])
            player = dados[8]
            send = f"2:{quit}:{reset}:{pos}:{up}:{right}:{bottom}:{left}:{player}"
            print(send)
            s.sendto(send.encode(), playerAddr(0))
            s.sendto(send.encode(), playerAddr(1))
                
            
            
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

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    
    esperando = True
    game = False
    while esperando:
        num_jogadores = len(fila_espera)
        print(f"Servidor UDP iniciado. Aguardando dados em {HOST}:{PORT}...")
        
        
        print(f"A fila de espera possui {num_jogadores} jogadores")
        print("Aguardando conexão de jogadores ...")

        data, addr = s.recvfrom(BUFFER_SIZE)
        print(f"Conexão recebida de {addr}")
        
        if(data):
            
            trata_mensagem(data, addr)
            
        if len(fila_espera) == 2:
            res = f"1:A partida {party} vai começar"
            
            print("Iniciando partida ...")
            sleep(3)
            print("Partida iniciada!")
            s.sendto(res.encode(), playerAddr(0))
            s.sendto(res.encode(), playerAddr(1))
            party += 1
            esperando = False
            game = True

    while game:
        data, addr = s.recvfrom(BUFFER_SIZE)
        if(data):
            trata_mensagem(data, addr)

