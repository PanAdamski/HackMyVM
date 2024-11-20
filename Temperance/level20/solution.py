import hashlib
import struct
import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)

    s.send(b'levelx20')

    hash = s.recv(1024).decode()
    print(hash)

    password_list = '50_rockyou.txt'

    for password in open(password_list):
        hashed = hashlib.md5(password.strip().encode()).hexdigest()
        if hashed == hash:
            print(f'{password}')

            s.send(password.encode())
            data4 = s.recv(1024)
            print(data4)
