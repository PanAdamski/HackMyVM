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

    s.send(b'levelx23')

    data2 = s.recv(1024)
    print(data2)
    raw_base = data2.decode()
    print(raw_base)
    decoded_base = base64.b64decode(raw_base)
    print(decoded_base)


    img = Image.open(io.BytesIO(decoded_base)).convert('RGBA')
    rgba_values = list(img.getdata())

    ascii_result = ''.join(chr(pixel[-1]) for pixel in rgba_values)

    s.send(ascii_result.encode())

    final_response = s.recv(1024)
    print(final_response.decode())
