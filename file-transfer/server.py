"""
Server side socket code.
Client sends data to server.
"""
import socket


TCP = True  # UDP if False
ADDRESS = ('0.0.0.0', 8123)


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen(5)  # number of simultananeous connections

    client, addr = server.accept()

    # confirm connection and receive file size header
    client.sendall(b'hi')
    file_size = client.recv(1024).decode()
    print(file_size)

    # confirm receipt and receive data
    client.sendall(b'got it')
    data = client.recv(1024).decode()
    print(data)

    # confirm receipt
    client.sendall(b'done')

    client.close()
    server.close()
