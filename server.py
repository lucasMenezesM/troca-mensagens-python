import socket

# Configurações
HOST = '127.0.0.1'  # localhost
PORT = 5050         # porta para escutar

# Cria o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor escutando em {HOST}:{PORT}...")

# Espera uma conexão
conn, addr = server_socket.accept()
print(f"Conectado por {addr}")

while True:
    data = conn.recv(1024)  # Recebe até 1024 bytes
    if not data:
        break
    print(f"Cliente disse: {data.decode()}")
    resposta = input("Responder: ")
    conn.sendall(resposta.encode())

conn.close()
