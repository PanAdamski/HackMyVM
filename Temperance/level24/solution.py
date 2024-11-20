import requests
import struct
import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)

    s.send(b'levelx24')

    data2 = s.recv(1024)
    url = data2.decode()

    r = requests.get(url)
    s.send(r.text.encode())
    data3 = s.recv(1024)
    print(data3)

