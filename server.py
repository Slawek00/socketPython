import socket as s
HOST = '127.0.0.1'
PORT = 65434
BUFFER = 1024
server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)


def fibb(n):
    result = [0, 1]
    for i in range(n-1):
        result.append(result[i] + result[(i + 1)])
        return result


while True:
    client_socket, address = server_socket.accept()
    print(f"Uzyskano połączenie od {address[0]}:{address[1]}")
    fib = client_socket.recv(BUFFER).decode("utf8")
    fibi = int(fib)
    fibs = str(fibb(fibi)).encode("utf8")
    client_socket.send(fibs)
    exit()