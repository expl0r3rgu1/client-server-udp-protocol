#!/usr/bin/python3

import socket
import os
from client_op import *

SERVER_ADDRESS = ('127.0.0.1', 10000)
BUFFER_SIZE = 1024
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    cmd = input("Enter command: ")
    print("")

    if cmd == "list":
        list_files(SERVER_SOCKET, SERVER_ADDRESS)
    elif cmd.startswith('get'):
        get_file(SERVER_SOCKET, SERVER_ADDRESS, cmd)
    elif cmd.startswith('put'):
        upload_file(SERVER_SOCKET, SERVER_ADDRESS, cmd)
    elif cmd == "exit":
        SERVER_SOCKET.sendto(cmd.encode(), SERVER_ADDRESS)
        SERVER_SOCKET.close()
        exit()
    else:
        print("Unknown command")

    print("")