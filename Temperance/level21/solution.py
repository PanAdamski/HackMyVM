import io
from PIL import Image
import struct
import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)

    s.send(b'levelx21')

    data2 = s.recv(1024).decode()
    print(data2)
    kb = int(data2) / 1024
    kb_data = f'{kb:.2f}'+'KB'

    s.send(kb_data.encode())
    data4 = s.recv(1024)
    print(data4)
