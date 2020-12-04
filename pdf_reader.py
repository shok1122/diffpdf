import tika
from tika import parser

class PdfReader:

    def __init__(self):
        pass

    def open(self, path):
        self.path = path
        self.parsed = parser.from_file(path)

    def get_text(self):
        return self.parsed['content']

