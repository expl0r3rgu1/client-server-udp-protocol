#!/usr/bin/python3

import socket
from _thread import *
import os

host = "127.0.0.1"
port = 10000
buffer_size = 1024

def client_handler(server_socket, cmd, addr):
    if cmd == "list":
        files = os.listdir('.')
        for file in files:
            server_socket.sendto(file.encode("utf-8"), addr)


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