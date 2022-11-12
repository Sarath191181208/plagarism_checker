import docx2txt
from .base_class import BaseParser
class WordParser(BaseParser):
    @staticmethod
    def parse(abs_file_name: str) -> str:
        with open(abs_file_name, mode='rb') as f:
             wordreader = docx2txt.process(f)
             return wordreader
 

    