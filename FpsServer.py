# Name:  Matthew Devery
# Class: CS 361
# Title: FPS Microservice Server

import json
import socket
import time


class HttpServer:
    MAX_FPS = 1000

    def __init__(self):
        self.Host = '127.0.0.1'
        self.Port = 9999
        self.Socket = None
        self._start_time = None
        self._count = 0
        self._fps = 0

    # Citation for this method:
    # Date: 7/29/2023
    # Adapted from:
    # Source URL: https://docs.python.org/3/howto/sockets.html
    # Source URL: https://docs.python.org/3/library/socket.html
    def start_server(self) -> None:
        """
        Starts the HTTP Server and listens for a request at the specified address. Then prints the address of the
        request, receives the first KiB, and sends the http response.
        """
        if self.Socket is None:
            self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.Socket.bind((self.Host, self.Port))

        running = True
        while running:
            self.Socket.listen(1)
            conn, addr = self.Socket.accept()
            print(f"Connected by {addr}")
            self._start_time = time.time()
            self._count = 0
            self._fps = 0

            with conn:
                conn_open = True
                while conn_open:
                    try:
                        conn.recv(1)
                        self.calculate_fps_data()
                        conn.sendall(json.dumps(self._fps).encode('utf-8'))
                    except ConnectionError:
                        conn_open = False

    def calculate_fps_data(self):
        self._count += 1
        current_time = time.time()
        try:
            self._fps = round(min(self._count / (current_time - self._start_time), self.MAX_FPS), 1)
        except ZeroDivisionError:
            self._fps = self.MAX_FPS


if __name__ == '__main__':
    my_http_server = HttpServer()
    my_http_server.start_server()
    input('Press Enter to close...')
