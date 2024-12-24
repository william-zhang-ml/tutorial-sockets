"""
Client side socket code.
Client sends a message to server and gets a response back.
"""
import socket


TCP = True  # UDP if False
ADDRESS = ('127.0.0.1', 8123)


if __name__ == '__main__':
    SOCKET_TYPE = socket.SOCK_STREAM if TCP else socket.SOCK_DGRAM
    client = socket.socket(socket.AF_INET, SOCKET_TYPE)

    if TCP:
        client.connect(ADDRESS)
        client.send('hello from client'.encode())
        print(client.recv(1024).decode())
    else:
        client.sendto('hello from client'.encode(), ADDRESS)
        data, addr = client.recvfrom(1024)  # this is blocking (cannot Ctrl-C)
        print(data.decode())
