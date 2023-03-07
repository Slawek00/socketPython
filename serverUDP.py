import socket as sock

HOST = '127.0.0.1'
PORT = 6595

serverUDP = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
serverUDP.bind((HOST, PORT))

while True:
    data, address = serverUDP.recvfrom(PORT)
    data = str(data, 'ascii')
    print(data)

