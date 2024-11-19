import codecs
import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)
    print(data)

    s.send(b'levelx09')

    data2 = s.recv(1024)
    print(data2)
    data3 = data2.decode()
    print(data3)
    data4 = codecs.encode(data3,'rot13')
    print(data4)

    s.send(data4.encode())
    data5 = s.recv(1024)
    print(data5)
