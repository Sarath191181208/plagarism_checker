from abc import ABC

class BaseParser(ABC):
    @staticmethod
    def parse(abs_file_name: str) -> str:
        """reads and returns the text of the given file"""