from itertools import permutations
import hashlib
import struct
import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)

    s.send(b'levelx32')

    output = s.recv(1024).decode()
    hash, to_permut = output.split()
    print(hash)
    print(to_permut)

    p = permutations(to_permut)

    for password in p:
        hashed = hashlib.md5(''.join(password).encode()).hexdigest()
        if hashed == hash:
            print(f'{password}')

            s.send(''.join(password).encode())
            data4 = s.recv(1024)
            print(data4)
'''
    for password in p:
        hashed = hashlib.md5(password.strip().encode()).hexdigest()
        if hashed == hash:
            print(f'{password}')

            s.send(password.encode())
            data4 = s.recv(1024)
            print(data4)
'''
