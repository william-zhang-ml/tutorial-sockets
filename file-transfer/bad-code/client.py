"""
Client side socket code.
Client sends data to server.
"""
import socket


TCP = True  # UDP if False
ADDRESS = ('127.0.0.1', 8123)
MESSAGE = 'thumbnail-perhaps.png'.encode()


def send_tcp(client: socket.socket, data: bytes) -> None:
    """Send client data to a server over TCP.

    Args:
        client (socket.socket): client socket
        data (bytes): data to send
    """
    client.sendall(str(len(data)).encode())  # server can anticipate
    client.sendall(data)
    client.sendall('<END>'.encode())


def send_udp(
    client: socket.socket,
    address: socket.socket,
    data: bytes
) -> None:
    """Send client data to a server over UDP.

    Args:
        client (socket.socket): client socket
        address (socket.socket): address to send to
        data (bytes): data to send
    """
    client.sendto(str(len(data)).encode(), address)  # server can anticipate
    client.sendto(data, address)
    client.sendto('<END>'.encode(), address)


if __name__ == '__main__':
    SOCKET_TYPE = socket.SOCK_STREAM if TCP else socket.SOCK_DGRAM
    client = socket.socket(socket.AF_INET, SOCKET_TYPE)

    if TCP:
        client.connect(ADDRESS)
        send_tcp(client, MESSAGE)
    else:
        send_udp(client, ADDRESS, MESSAGE)

    client.close()
