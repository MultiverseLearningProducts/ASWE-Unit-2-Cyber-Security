import unittest
import requests
import logging
from io import StringIO
from unittest.mock import patch
from server import start_server, handle_client

class TestATMServer(unittest.TestCase):
    def setUp(self):
        self.host = 'localhost'
        self.port = 8000
        self.base_url = f'http://{self.host}:{self.port}'

    def test_server_listening(self):
        with patch('builtins.print') as mock_print:
            start_server()
            mock_print.assert_called_with(f"Server is listening on {self.host}:{self.port}")

    def test_get_request_response(self):
        with patch('builtins.print') as mock_print:
            response = requests.get(f'{self.base_url}/transaction')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                'transaction_id': '12345',
                'amount': 100.00,
                'status': 'success'
            })
            mock_print.assert_called_with(f"Received GET request for /transaction from ('127.0.0.1', {self.port})")

    def test_invalid_request_response(self):
        response = requests.get(f'{self.base_url}/invalid')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, 'Resource not found')

    def test_client_request_logging(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('logging.FileHandler', return_value=logging.StreamHandler(fake_output)):
                handle_client(None)
                self.assertIn('Received GET request for /transaction from', fake_output.getvalue())

if __name__ == '__main__':
    unittest.main()
