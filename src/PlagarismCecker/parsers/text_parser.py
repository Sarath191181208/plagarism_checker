from .base_class import BaseParser

class TxtParser(BaseParser):
    @staticmethod
    def parse(abs_file_name: str) -> str:
        with open(abs_file_name) as stream:
            return stream.read()