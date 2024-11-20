import base64
import socket
from io import BytesIO
from pyzbar.pyzbar import decode
from PIL import Image

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)

    s.send(b'levelx31')

    raw_base = s.recv(1024).decode()
    print(raw_base)
    qr_code = base64.b64decode(raw_base)
    print(f"Zdekodowany QR Code: {qr_code}")

    image = Image.open(BytesIO(qr_code))

    decoded_objects = decode(image)
    final_value = decoded_objects[0].data.decode()
    print(final_value)

    s.send(final_value.encode())
    data4 = s.recv(1024)
    print(data4)
