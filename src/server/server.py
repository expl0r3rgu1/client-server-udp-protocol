#!/usr/bin/python3

import socket
import threading
import os

host = "127.0.0.1"
port = 10000
buffer_size = 1024

def client_handler(server_socket, cmd, addr):
    if cmd == "list":
        files = os.listdir('./files')
        server_socket.sendto(str(len(files)).encode("utf-8"), addr)
        for file in files:
            server_socket.sendto(file.encode("utf-8"), addr)
    
    elif cmd.startswith('get'):
        filename = cmd.split()[1]
        if os.path.exists('./files/' + filename):
            server_socket.sendto("OK".encode("utf-8"), addr)
            file = open("./files/" + filename, 'rb')
            while True:
                data = file.read(buffer_size)
                if not data:
                    server_socket.sendto("EOF".encode("utf-8"), addr)
                    break
                server_socket.sendto(data, addr)
            file.close()
        else:
            server_socket.sendto("NOT OK".encode("utf-8"), addr)
    elif cmd.startswith('put'):
        filename = cmd.split()[1]
        file = open("./files/" + filename, 'wb')
        while True:
            data, addr = server_socket.recvfrom(buffer_size)
            if data.decode("utf-8") == "EOF":
                break
            file.write(data)

        file.close()
    elif cmd == "exit":
        server_socket.close()
        exit()
    else:
        server_socket.sendto("Unknown command".encode("utf-8"), addr)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Server started and listening on port: " + str(port))

    while True:
        data, addr = server_socket.recvfrom(buffer_size)
        cmd = data.decode("utf-8")
        print("Received message from: " + str(addr))
        print("Message: " + cmd)
        thread = threading.Thread(target=client_handler, args=(server_socket, cmd, addr))
        thread.start()
        thread.join()

start_server()