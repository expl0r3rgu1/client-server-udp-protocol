# server operations
FILES_PATH = './files'
EOF = b' /EOF/ \r\n/'
BUFFER_SIZE = 1024

def list_files(server_socket, addr):
    files = os.listdir(FILES_PATH)
    server_socket.sendto(str(len(files)).encode("utf-8"), addr)
    for file in files:
        server_socket.sendto(file.encode("utf-8"), addr)
    print("List of files sent")

def send_file(server_socket, filename, addr):
    if os.path.exists(FILES_PATH + '/' + filename):
        print("Sending file: " + filename)
        server_socket.sendto("OK".encode("utf-8"), addr)
        file = open(FILES_PATH + '/' + filename, 'rb')
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                server_socket.sendto(EOF, addr)
                break
            server_socket.sendto(data, addr)
        file.close()
        print("File " + filename + " sent")
    else:
        server_socket.sendto("NOT OK".encode("utf-8"), addr)

def update_file(server_socket, filename, addr):
    print("Receiving file: " + filename)
    file = open(FILES_PATH + '/' + filename, 'wb')
    while True:
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        if data == EOF:
            break
        file.write(data)
    file.close()
    print("File " + filename + " received")