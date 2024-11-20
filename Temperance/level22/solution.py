import struct
import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)
    print(data)

    s.send(b'levelx22')

    data2 = s.recv(1024)
    print(data2)
    data3 = data2.decode().strip()
    numbers = data3.split()

    wynik = ''.join(chr(int(num)) for num in numbers)

    s.send(wynik.encode())
    data4 = s.recv(1024)
    print(data4)
