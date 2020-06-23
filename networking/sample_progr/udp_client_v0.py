import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"ayam den lapeh", ("127.0.0.1", 5000))
