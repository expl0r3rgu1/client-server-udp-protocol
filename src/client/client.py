#!/usr/bin/python3

import socket
import os

SERVER_ADDRESS = ('127.0.0.1', 10000)
BUFFER_SIZE = 1024
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    cmd = input("Enter command: ")
    print("")

    if cmd == "list":
        list_files(server_socket, addr)
    elif cmd.startswith('get'):
        get_file(server_socket, addr, cmd)
    elif cmd.startswith('put'):
        upload_file(server_socket, addr, cmd)
    elif cmd == "exit":
        server_socket.sendto(cmd.encode(), server_address)
        server_socket.close()
        exit()
    else:
        print("Unknown command")

    print("")