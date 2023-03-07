import socket

HOST = '127.0.0.1'
PORT = 6595

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
communication_socket, address = server.accept()

while True:
    message = communication_socket.recv(1024).decode('utf-8')
    if not message:
        break
    print(f"Message from client is: {message}")
communication_socket.close() #aby nie było problemów z portem
