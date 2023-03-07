import socket, time, serial

HOST = '127.0.0.1'
PORT = 6595

clientUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
arduino = serial.Serial("COM3", 9600)
time.sleep(2)

while True:
    data = arduino.readline()[0:4]
    clientUDP.sendto(data, (HOST, PORT))
