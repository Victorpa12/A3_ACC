import socket

HOST = '127.0.0.1'
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode('0:Hello, world'))
i = 1
while True:
    data = s.recv(1024)
    decData = data.decode()
    dados = decData.split(':')
    
    print('mensagem ecoada: ', data.decode())

    if data:
    
        s.sendall(str.encode(f'{i}:Hello, mundo'))
        i += 1
        j = int(dados[0])
        msg = dados[1]
    
        if j == 10:
            break
    





