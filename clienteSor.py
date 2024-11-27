import socket  # Importa o módulo socket, que permite a comunicação de rede.

# Define o endereço do servidor e a porta que será utilizada para a comunicação.
SERVER_HOST = "localhost"
SERVER_PORT = 4000

# Define o tamanho do buffer para a recepção de dados.
BUFFER_SIZE = 1024

def main():
    # Define a mensagem que será enviada ao servidor.
    msg = "1:meu nome é Patati"

    # Cria um socket UDP (User Datagram Protocol).
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Envia a mensagem codificada em bytes para o endereço e porta especificados.
    skt.sendto(msg.encode(), (SERVER_HOST, SERVER_PORT))

# Verifica se o script está sendo executado diretamente (não importado como módulo).
if __name__ == "__main__":
    main()  # Chama a função main para executar o código.