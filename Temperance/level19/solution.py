import zipfile

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

    s.send(b'levelx19')

    data2 = s.recv(1024)
    print(data2)
    raw_base = data2.decode()
    print(raw_base)
    zip_data = base64.b64decode(raw_base)

    with zipfile.ZipFile(io.BytesIO(zip_data)) as zip_file:
        file_names = zip_file.namelist()
        print("Pliki w archiwum ZIP:", file_names)

        for file_name in file_names:
            if file_name.endswith('.txt'):
                with zip_file.open(file_name) as txt_file:
                    content = txt_file.read().decode('utf-8')


    print(content)

    s.send(content.encode())
    data4 = s.recv(1024)
    print(data4)
