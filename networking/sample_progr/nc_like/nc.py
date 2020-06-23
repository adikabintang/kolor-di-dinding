import server, sys, socket, getopt

class TcpServer(server.AbstractTcpServer):
    def handle_data(self, socket, conn, data):
        print("tcp, from: {}, data: {}".format(conn, data))

class UdpServer(server.AbstractUdpServer):
    def handle_data(self, socket, conn, data):
        print("udp, from: {}, data: {}".format(conn, data)) 

def run_tcp_client(addr: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((addr, port))
        
        for line in sys.stdin:
            s.sendall(line.encode("utf-8"))

def run_udp_client(addr: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        for line in sys.stdin:
            s.sendto(line.encode("utf-8"), (addr, port))

if __name__ == "__main__":
    try:
        is_server = False
        is_udp = False
        server = None
        opts, args = getopt.getopt(sys.argv[1:], "ul")
        
        for key, val in opts:
            if key == "-l":
                is_server = True
            elif key == "-u":
                is_udp = True
        
        if is_server:
            if is_udp:
                server = UdpServer()
            else:
                server = TcpServer()

            server.start()
        else:
            if len(args) < 2:
                print("specify ip addr and port")
                sys.exit(2)
            
            if is_udp:
                run_udp_client(args[0], args[1])
            else:
                run_tcp_client(args[0], args[1])

    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
