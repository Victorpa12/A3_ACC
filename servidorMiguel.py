import socket

HOST = '127.0.0.1'
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print(f"Servidor iniciado. Aguardando conexão em {HOST}:{PORT}...")
conn, addr = s.accept()

print(f"Conexão recebida de {addr}")

while True:
    data = conn.recv(1024)
    decData = data.decode()
    dados = decData.split(':')

    i = int(dados[0])
    msg = dados[1]
    
    if i > 10:
        break

    res = (f"{i}: responta: {data.decode()}")
    print(f"Recebido: {data.decode()}")
    conn.sendall(res.encode())
    
    

