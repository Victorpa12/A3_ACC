import socket
import pygame

HOST = '127.0.0.1'
PORT = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# msg =(f"1:{input('Digite seu nome: ')}") 
msg = "1: Patati"
s.sendto(msg.encode(), (HOST, PORT))
data = s.recv(1024)
if data:
    print('Mensagem recebida do servidor:', data.decode())



# for event in pygame.event.get():  # Para cada evento
#         if event.type == pygame.QUIT:  # Se o evento é para sair
#             quit = True  # Define a flag de saída

#         if event.type == pygame.MOUSEBUTTONDOWN:  # Se o botão do mouse foi pressionado
#             pos = event.pos  # Posição do clique

#         if event.type == pygame.MOUSEBUTTONUP:  # Se o botão do mouse foi solto
#             pos = None  # Reseta a posição após soltar o mouse

#         if event.type == pygame.KEYDOWN:  # Se uma tecla foi pressionada
#             if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:  # Se a tecla é 'q' ou 'ESC'
#                 quit = True
#             if event.key == pygame.K_r:  # Se a tecla é 'r'
#                 reset = True  # Define a flag de reset
                
            
#             if event.key == pygame.K_UP: up = True  # Se a tecla é 'UP'
#             if event.key == pygame.K_RIGHT: right = True  # Se a tecla é 'RIGHT'
#             if event.key == pygame.K_DOWN: bottom = True  # Se a tecla é 'DOWN'
#             if event.key == pygame.K_LEFT: left = True  # Se a tecla é 'LEFT'

#         if event.type == pygame.KEYUP:  # Se uma tecla foi solta
#             if event.key == pygame.K_UP: up = False  # Reseta a direção 'UP'
#             if event.key == pygame.K_RIGHT: right = False  # Reseta a direção 'RIGHT'
#             if event.key == pygame.K_DOWN: bottom = False  # Reseta a direção 'DOWN'
#             if event.key == pygame.K_LEFT: left = False  # Reseta a direção 'LEFT'




# s.sendall(str.encode(f'{quit}:{reset}:{pos}:{up}:{right}:{bottom}:{left}'))

# data = s.recv(1024)
# decData = data.decode()
# dados = decData.split(':')
# win = bool(dados[0])

# while True:
    
    
#     print('mensagem ecoada: ', data.decode())

#     if data:
    
#         s.sendall(str.encode(f'{i}:Hello, mundo'))
#         i += 1
        
    
#         if j == 10:
#             break
    





