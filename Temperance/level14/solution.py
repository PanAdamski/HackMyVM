import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)
    print(data)

    s.send(b'levelx14')

    data2 = s.recv(1024)
    print(data2)
    data3 = data2.decode()
    ciag, znak = map(str, data3.split())
    print(ciag)
    print(znak)
    data4 = ciag.count(znak)
    print(data4)

    s.send(str(data4).encode())
    data5 = s.recv(1024)
    print(data5)

