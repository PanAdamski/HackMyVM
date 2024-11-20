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

    s.send(b'levelx18')

    data2 = s.recv(1024)
    print(data2)
    raw = data2.decode()
#    binarnie = ''.join(format(ord(x), 'b') for x in raw)
    binarnie = ''.join(format(ord(x), '08b') for x in raw)
    print(binarnie)


    s.send(binarnie.encode())
    data3 = s.recv(1024)
    print(data3.decode())
