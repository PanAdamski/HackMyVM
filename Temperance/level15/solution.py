import struct  
import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)
    print(data)

    s.send(b'levelx15')

    data2 = s.recv(1024)
    print(data2)

    numbers = list(map(int, data2.split()))
    roznica = numbers[-1] - numbers[-2]
    nowa_liczba = numbers[-1] + roznica

    data3 = str(nowa_liczba).encode()
    s.send(data3)
    data4 = s.recv(1024)
    print(data4)
