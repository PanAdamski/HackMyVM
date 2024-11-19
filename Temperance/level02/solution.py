import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx02')

    data2 = s.recv(1024)
    print(data2)

    s.send(data2.upper())
    data3 = s.recv(1024)
    print(data3)
