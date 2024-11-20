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

    s.send(b'levelx17')

    data2 = s.recv(1024)
    print(data2)
    raw_base = data2.decode()
    print(raw_base)
    decoded_base = base64.b64decode(raw_base)
    print(decoded_base)


    img = Image.open(io.BytesIO(decoded_base)).convert('RGBA')
    background = Image.new('RGBA', img.size, (255, 255, 255))

    pixel_data = list(img.getdata())
    last_rgba = pixel_data[-1]
    print(last_rgba[-1])

    s.send(str(last_rgba[-1]).encode())
    data4 = s.recv(1024)
    print(data4)
