import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)
    print(data)

    s.send(b'levelx05')

    data2 = s.recv(1024)
    print(data2)
    data3 = data2.decode()[-5:]

    s.send(data3.encode())
    data4 = s.recv(1024)
    print(data4)
