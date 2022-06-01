#!/usr/bin/python3

FILES_PATH = './files'
EOF = b' /EOF/ \r\n/'
BUFFER_SIZE = 1024

def list_files(server_socket, server_address, cmd):
    server_socket.sendto(cmd.encode(), server_address)
    data, addr = server_socket.recvfrom(BUFFER_SIZE)
    files_num = int(data.decode("utf-8"))

    print("Received files number: " + str(files_num))
    for file in range(files_num):
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        print(data.decode("utf-8"))

def get_file(server_socket, server_address, cmd):
    server_socket.sendto(cmd.encode(), server_address)
    filename = cmd.split()[1]
    data, addr = server_socket.recvfrom(BUFFER_SIZE)

    if data.decode("utf-8") == "OK":
        print("Downloading file: " + filename)
        if not os.path.isdir(FILES_PATH):
            os.mkdir(FILES_PATH)
        file = open(FILES_PATH + filename, 'wb')
        while True:
            data, addr = server_socket.recvfrom(BUFFER_SIZE)
            if data == EOF:
                break
            file.write(data)

        file.close()
        print("File " + filename + " received")
    else:
        print("File not found")

def upload_file(server_socket, server_address, cmd):
    server_socket.sendto(cmd.encode(), server_address)
    filename = cmd.split()[1]
    if os.path.exists(FILES_PATH + filename):
        print("Uploading file: " + filename)
        server_socket.sendto(cmd.encode(), server_address)
        file = open(FILES_PATH + filename, 'rb')
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                server_socket.sendto(eof, server_address)
                break
            server_socket.sendto(data, server_address)
        file.close()
        print("File " + filename + " uploaded")
    else:
        print("File not found")