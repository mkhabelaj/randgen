import socket


class Generator:

    def __init__(self, address='0.0.0.0', min_range=5000, max_range=6000,number_of_ports=1):
        self.in_use = []
        self.min_range = min_range
        self.max_range = max_range
        self.number_of_ports = number_of_ports
        self.address = address

    def produce_ports(self):
        result = []

    def validate_port(self, port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((self.address, port))
            client_socket.close()
            return False
        except Exception as ex:
            return True




