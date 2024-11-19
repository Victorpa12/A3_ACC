import socket

SERVER_HOST = "localhost"
SERVER_PORT = 1234

BUFFER_SIZE = 1024

def main():

    msg = "1:meu nome é Patati"

    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    skt.sendto(msg.encode(), (SERVER_HOST, SERVER_PORT))


if __name__ == "__main__":
    main()