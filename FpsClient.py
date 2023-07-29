# Name:  Matthew Devery
# Class: CS 361
# Title: FPS Microservice Client

import socket
import time


# Citation for this class and its methods:
# Date: 7/29/2023
# Adapted from:
# Source URL: https://docs.python.org/3/howto/sockets.html
# Source URL: https://docs.python.org/3/library/socket.html
class FpsClient:
    def __init__(self):
        self.Host = '127.0.0.1'
        self.Port = 9999
        self.Socket = None

    def connect(self) -> None:
        """
        Connects the UMassSocket to the host on the default http port 80.
        """
        if self.Socket is None:
            self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.Socket.connect((self.Host, self.Port))

    def get_fps(self) -> str:
        """
        Sends the given http request using the connected socket and receives a 1024B response which is printed to the
        console.
        """
        if self.Socket is None:
            self.connect()

        self.Socket.sendall('1'.encode("utf-8"))
        response = self.Socket.recv(5).decode()
        return response

    def close(self) -> None:
        """
        Closes the connected socket.
        """
        self.Socket.shutdown(1)
        self.Socket.close()


if __name__ == '__main__':
    client = FpsClient()
    client.connect()
    for _ in range(10):
        print(client.get_fps())
        time.sleep(0.1)
    client.close()
    input("Press Enter...")
