import re
import requests
import struct
import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)
    s.send(b'levelx27')

    data2 = s.recv(1024)
    url = data2.decode()
    print(url)
    r = requests.get(url)
    print(r.text)
    number = re.search(r'proxy:x:([0-9]+):',r.text).group(1)
    print(number)


    s.send(number.encode())
    data3 = s.recv(1024)
    print(data3)
