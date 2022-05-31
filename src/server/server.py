#!/usr/bin/python3

import socket
from _thread import *

host = "127.0.0.1"
port = 10000
buffer_size = 1024

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Server started and listening on port: " + str(port))

    while True:
        data, addr = server_socket.recvfrom(buffer_size)
        cmd = data.decode("utf-8")
        print("Received message from: " + str(addr))
        print("Message: " + cmd)

start_server()