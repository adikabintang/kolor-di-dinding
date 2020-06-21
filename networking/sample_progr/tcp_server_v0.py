# from here: https://realpython.com/python-sockets/

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 8080))
    
    # s.listen(backlog), default = 5
    # what is backlog: https://stackoverflow.com/a/18073744/10522825
    # number of QUEUED connections on a socket
    s.listen()

    # accept returns a new socket when there is a client connecting to here. 
    # this new socket is the way we talk to the client
    conn, addr = s.accept()
    with conn:
        print("connected by: ", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
