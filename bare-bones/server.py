"""
Server side socket code.
Client sends a message to server and gets a response back.
"""
import socket


TCP = False  # UDP if False


if __name__ == '__main__':
    SOCKET_TYPE = socket.SOCK_STREAM if TCP else socket.SOCK_DGRAM
    server = socket.socket(socket.AF_INET, SOCKET_TYPE)
    server.bind(('127.0.0.1', 8123))

    if TCP:
        server.listen(5)  # number of simultananeous connections
        client, addr = server.accept()  # this is blocking (cannot Ctrl-C)
        print(f'{addr}: {client.recv(1024).decode()}')
        client.send('hello from server'.encode())
    else:
        data, addr = server.recvfrom(1024)  # this is blocking (cannot Ctrl-C)
        print(f'{addr}: {data.decode()}')
        server.sendto('hello from server'.encode(), addr)
