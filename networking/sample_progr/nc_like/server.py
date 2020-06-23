import socket
from abc import ABC, abstractmethod

class AbstractTcpServer(ABC):
    def __init__(self, addr="127.0.0.1", port=8080):
        self.listen_addr = addr
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.listen_addr, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1500)
                    if not data:
                        break
                    self.handle_data(conn, addr, data)
    
    @abstractmethod
    def handle_data(self, socket, conn, data):
        pass

class AbstractUdpServer(ABC):
    def __init__(self, addr="127.0.0.1", port=8080):
        self.listen_addr = addr
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.listen_addr, self.port))
            while True:
                data, conn = s.recvfrom(1500)
                self.handle_data(s, conn, data)
    
    @abstractmethod
    def handle_data(self, socket, conn, data):
        pass