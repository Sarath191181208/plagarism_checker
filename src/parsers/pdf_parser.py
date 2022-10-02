import PyPDF2
from .base_class import BaseParser

class PdfParser(BaseParser):
    @staticmethod
    def parse(abs_file_name: str) -> str:
        with open(abs_file_name, mode='rb') as f:
            pdfReader = PyPDF2.PdfFileReader(f)
            pages_txt = [pdfReader.getPage(i).extractText() for i in range(pdfReader.numPages)]
            txt = "\n".join(pages_txt)
        return txt