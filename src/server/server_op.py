# server operations
FILES_PATH = './files'

def list_files(server_socket, cmd, addr):
    files = os.listdir(FILES_PATH)
    server_socket.sendto(str(len(files)).encode("utf-8"), addr)
    for file in files:
        server_socket.sendto(file.encode("utf-8"), addr)
    print("List of files sent")
