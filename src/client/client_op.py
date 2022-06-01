#!/usr/bin/python3

FILES_PATH = './files'
EOF = b' /EOF/ \r\n/'
BUFFER_SIZE = 1024

def list_files(server_socket, addr):
    server_socket.sendto(cmd.encode(), server_address)
    data, addr = server_socket.recvfrom(buffer_size)
    files_num = int(data.decode("utf-8"))

    print("Received files number: " + str(files_num))
    for file in range(files_num):
        data, addr = server_socket.recvfrom(buffer_size)
        print(data.decode("utf-8"))