"""
Server side socket code.
Client sends a message to server and gets a response back.
"""
import socket


TCP = True  # UDP if False
ADDRESS = ('0.0.0.0', 8123)


if __name__ == '__main__':
    SOCKET_TYPE = socket.SOCK_STREAM if TCP else socket.SOCK_DGRAM
    server = socket.socket(socket.AF_INET, SOCKET_TYPE)
    server.bind(ADDRESS)

    if TCP:
        server.listen(5)  # number of simultananeous connections
        client, addr = server.accept()

    if TCP:
        file_size = client.recv(1024).decode()
    else:
        file_size, _ = server.recvfrom(1024)
        file_size = file_size.decode()
    print(file_size)

    file_bytes = b''
    while True:
        if TCP:
            file_bytes += client.recv(1024)
        else:
            file_bytes += server.recvfrom(1024)[0]

        if file_bytes[-5:] == b'<END>':
            break
    print(file_bytes.decode())

    if TCP:
        client.close()
    server.close()
