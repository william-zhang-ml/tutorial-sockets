"""
Client side socket code.
Client sends a message to server and gets a response back.
"""
import socket


TCP = False  # UDP if False


if __name__ == '__main__':
    SOCKET_TYPE = socket.SOCK_STREAM if TCP else socket.SOCK_DGRAM
    client = socket.socket(socket.AF_INET, SOCKET_TYPE)

    if TCP:
        client.connect(('127.0.0.1', 8123))
        client.send('hello from client'.encode())
        print(client.recv(1024).decode())
    else:
        client.sendto('hello from client'.encode(), ('127.0.0.1', 8123))
        data, addr = client.recvfrom(1024)  # this is blocking (cannot Ctrl-C)
        print(data.decode())
