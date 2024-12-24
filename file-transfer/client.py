"""
Client side socket code.
Client sends data to server.
"""
import socket


ADDRESS = ('127.0.0.1', 8123)
MESSAGE = 'thumbnail-perhaps.png'.encode()


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)

    # wait for server confirmation and send file size header
    confirm = client.recv(1024)
    if confirm == b'hi':
        client.sendall(str(len(MESSAGE)).encode())

    # wait for server confirmation and send data
    confirm = client.recv(1024)
    if confirm == b'got it':
        client.sendall(MESSAGE)

    # wait for server confirmation
    confirm = client.recv(1024)
    if confirm == b'done':
        client.close()

    client.close()
