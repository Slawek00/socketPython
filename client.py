import socket as s
HOST = '127.0.0.1'
PORT = 65434
BUFFER = 1024

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Podaj numer krańcowego wyrazu:")
op = input().encode("utf8")
client_socket.send(op)

print("Twój ciąg Fibonacciego:")
fibop = client_socket.recv(BUFFER).decode("utf8")
print(fibop)