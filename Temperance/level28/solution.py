import jwt
import requests
import struct
import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)

    s.send(b'levelx28')

    data2 = s.recv(1024)
    jwt_token = data2.decode()
    print(jwt_token)
    payload = jwt.decode(jwt_token, options={"verify_signature": False})

    result = payload["HMVKey"]
    print(result)

    s.send(result.encode())
    data3 = s.recv(1024)
    print(data3)
