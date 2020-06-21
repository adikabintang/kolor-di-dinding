# https://wiki.python.org/moin/UdpCommunication
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(("0.0.0.0", 8080))
    while True:
        data, addr_n_port = s.recvfrom(1024) # 1024 is the buffer size
        print("from: {}, data: {}".format(addr_n_port, data))
