import re
from geopy.distance import geodesic
import requests
import struct
import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)

    s.send(b'levelx29')

    data2 = s.recv(1024).decode()
    pattern = r"Lat:\s*(-?\d+(\.\d+)?)\s*Lon:\s*(-?\d+(\.\d+)?)"

    matches = re.findall(pattern, data2)

    if matches:
        lat1, lon1 = float(matches[0][0]), float(matches[0][2])
        lat2, lon2 = float(matches[1][0]), float(matches[1][2])

    point1 = (lat1, lon1)
    point2 = (lat2, lon2)
    distance = geodesic(point1, point2).kilometers
    wynik = f'{distance:.3f}'

    s.send(wynik.encode())
    data3 = s.recv(1024)
    print(data3)
