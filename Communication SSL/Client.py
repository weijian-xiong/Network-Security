import socket, ssl

HOST, PORT, server_sni_hostname = '127.0.0.1', 443, 'Weijian Xiong'
server_cert = 'cert.pem'


def handle(conn):
    conn.write(b'GET / HTTP/1.1\n')
    print(conn.recv().decode())
    print('client successfully connected!')

def main():

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_cert)
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = context.wrap_socket(sock,server_side=False, server_hostname=server_sni_hostname)
    try:
        conn.connect((HOST, PORT))
        handle(conn)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
