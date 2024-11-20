import base64
from io import BytesIO
from PIL import Image
import pytesseract
import requests
import struct
import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)

    s.send(b'levelx26')

    data2 = s.recv(1024).decode()
    print(data2)
    image_data = base64.b64decode(data2)

    image = Image.open(BytesIO(image_data))

    extracted_text = pytesseract.image_to_string(image)
    s.send(extracted_text.encode())
    data3 = s.recv(1024)
    print(data3)
