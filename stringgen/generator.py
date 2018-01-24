import random
import socket
import string


class StringGenerator:

    def __init__(self, string_length=20):
        self.string_length = string_length

    def produce_strings(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(self.string_length))





