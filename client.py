import socket

# Configurações
HOST = '127.0.0.1'  # IP do servidor
PORT = 5050         # mesma porta

# Cria o socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Conectado ao servidor.\n")

while True:
    msg = input("Você: ")
    client_socket.sendall(msg.encode())
    resposta = client_socket.recv(1024)
    print("Servidor:", resposta.decode())
