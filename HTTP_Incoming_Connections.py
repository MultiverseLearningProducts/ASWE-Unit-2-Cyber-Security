import socket

def start_server():
    host = 'localhost'
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address}")
        handle_client(client_socket)

def handle_client(client_socket):
    # Handle client requests here
    pass

if __name__ == '__main__':
    start_server()
