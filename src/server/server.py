#!/usr/bin/python3

import socket
import threading
import os
from server_op import *

HOST = "127.0.0.1"
PORT = 10000
BUFFER_SIZE = 1024

def client_handler(server_socket, cmd, addr):
    if cmd == "list":
        list_files(server_socket, addr)
    elif cmd.startswith('get'):
        filename = cmd.split()[1]
        send_file(server_socket, filename, addr)
    elif cmd.startswith('put'):
        filename = cmd.split()[1]
        update_file(server_socket, filename, addr)
    else:
        server_socket.sendto("Unknown command".encode("utf-8"), addr)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))

    print("Server started and listening on port: " + str(PORT))

    while True:
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        cmd = data.decode("utf-8")
        print("Received message from: " + str(addr))
        print("Message: " + cmd)
        if cmd == "exit":
            server_socket.close()
            exit()
        thread = threading.Thread(target=client_handler, args=(server_socket, cmd, addr))
        thread.start()
        thread.join()

start_server()