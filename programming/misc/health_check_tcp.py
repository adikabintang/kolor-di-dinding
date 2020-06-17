import socket

all_ip_addr = ["127.0.0.1", "127.0.0.1"]
all_ports = [5000, 80]
all_failed = []

for ip, port in zip(all_ip_addr, all_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    probe = sock.connect_ex((ip, port))
    sock.close()
    if probe != 0:
        all_failed.append((ip, port))

print(all_failed)
