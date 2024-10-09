import socket

class Cliente:
    def __init__(self, nome, host="localhost", porta=5555):
        self.nome = nome
        self.host = host
        self.porta = porta
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def conectar(self):
        try:
            self.cliente.connect((self.host, self.porta))
            self.cliente.send(self.nome.encode())
            print(f"Conectado como {self.nome}")
            self.escutar_servidor()
        except Exception as e:
            print(f"Erro ao conectar: {e}")
    
    def escutar_servidor(self):
        while True:
            mensagem = self.cliente.recv(1024).decode()
            print(mensagem)
            if "Sua vez" in mensagem:
                movimento = input("Digite o movimento (linha,coluna): ")
                self.cliente.send(movimento.encode())

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    cliente = Cliente(nome)
    cliente.conectar()
