import socket, serial, time

#HOST = '192.168.0.18'
HOST = '127.0.0.1'
PORT = 6595

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((HOST, PORT))

arduino = serial.Serial("COM3", 9600)
time.sleep(2)

while True:
    data = arduino.readline()[0:4]
    cli.send(str(data).encode('utf-8'))








