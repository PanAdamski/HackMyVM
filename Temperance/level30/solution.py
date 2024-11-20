import requests
import struct
import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)

    s.send(b'levelx30')

    data2 = s.recv(1024)
    print(data2)
    
    key = "HMV"
    result = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data2.decode()))
    print(result)
    s.send(result.encode())
    data3 = s.recv(1024)
    print(data3)
