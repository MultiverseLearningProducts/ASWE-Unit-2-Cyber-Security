import logging

def setup_logging():
    logging.basicConfig(filename='atm_server.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    headers = request.split('\n')
    method, path, _ = headers[0].split()

    client_address = client_socket.getpeername()
    log_message = f"Received {method} request for {path} from {client_address}"
    logging.info(log_message)

    # Process the request and send the response
    # ...

if __name__ == '__main__':
    setup_logging()
    start_server()
