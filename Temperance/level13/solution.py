import struct  
import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)
#    print(data)

    s.send(b'levelx13')

    data2 = s.recv(1024)
    data3 = data2.decode()
    cleaned_data = data3.replace("[", "").replace("]", "")
    cleaned_data = cleaned_data.replace("\n", "").replace("\r", "").strip()
    elements = cleaned_data.split(" ")
    elements.sort()

    print(elements)


    s.send(str(elements[-1]).encode())
    data4 = s.recv(1024)
    print(data4)

