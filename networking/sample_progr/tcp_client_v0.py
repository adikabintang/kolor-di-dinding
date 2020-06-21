# https://realpython.com/python-sockets/

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 8080))
    
    # why sendall() instead of send()?
    # loook at the server's recv(). it's buffer is 1024. if send() sends
    # more than 1024 bytes, not all data will be sent and the sent() returns
    # number of unsent bytes. we can use loop to call send() repeatitively. 
    # sendall() sends all.
    s.sendall(b'asdf')
    
    data = s.recv(1024)

print("received: ", repr(data))
