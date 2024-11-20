import struct
import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)
    print(data)

    s.send(b'levelx22')

    data2 = s.recv(1024)
    print(data2)
    data3 = data2.decode()
    for x in data3:
       print(''.join(x))

'''
    s.send(ord(data3))
    data4 = s.recv(1024)
    print(data4)
'''
