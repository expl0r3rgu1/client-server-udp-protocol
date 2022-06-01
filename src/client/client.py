#!/usr/bin/python3

import socket
import os

SERVER_ADDRESS = ('127.0.0.1', 10000)
BUFFER_SIZE = 1024
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)