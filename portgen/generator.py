import socket
from random import *


class Generator:

    def __init__(self, address='0.0.0.0', min_range=5000, max_range=6000, number_of_ports=1):
        self.in_use = []
        self.min_range = min_range
        self.max_range = max_range
        self.number_of_ports = number_of_ports
        self.address = address

    def produce_ports(self):
        result = []
        counter = 0
        while counter < self.number_of_ports:
            port = self.generate_port()
            if port not in result and port not in self.in_use and self.validate_port(port):
                counter += 1
                result.append(port)
                self.in_use.append(port)
        return result

    def generate_port(self):
        return randint(self.min_range, self.max_range)

    def validate_port(self, port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((self.address, port))
            client_socket.close()
            return False
        except Exception as ex:
            return True