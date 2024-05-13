import json

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received request: {request}")

    headers = request.split('\n')
    method, path, _ = headers[0].split()

    if method == 'GET':
        if path == '/transaction':
            response_data = {
                'transaction_id': '12345',
                'amount': 100.00,
                'status': 'success'
            }
            response_body = json.dumps(response_data)
            response_headers = [
                'HTTP/1.1 200 OK',
                'Content-Type: application/json',
                f'Content-Length: {len(response_body)}'
            ]
            response = '\n'.join(response_headers) + '\n\n' + response_body
        else:
            response = 'HTTP/1.1 404 Not Found\n\nResource not found'
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\nMethod not allowed'

    client_socket.send(response.encode('utf-8'))
    client_socket.close()
