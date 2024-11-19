import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx01')

    data2 = s.recv(1024)
    print(data2)

    s.send(data2)
    data3 = s.recv(1024)
    print(data3)
    
    s.send(data3)
    data4 = s.recv(1024)
    print(data4)


    s.send(b'ImString1!')
    data5 = s.recv(1024)
    print(data5)
