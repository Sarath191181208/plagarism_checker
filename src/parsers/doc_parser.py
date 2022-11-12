import docx
from .base_class import BaseParser
class WordParser(BaseParser):
    @staticmethod
    def parse(abs_file_name: str) -> str:
        doc = docx.Document(abs_file_name)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)
 

    