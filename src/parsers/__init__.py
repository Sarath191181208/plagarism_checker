import logging
from .text_parser import TxtParser
from .pdf_parser import PdfParser
from .excel_parser import ExcelParser
from .ppt_parser import PptParser
from .doc_parser import WordParser

from typing import Callable


def get_parser(file_name: str) -> Callable[str, str]:
    """returns the parser for the given file"""
    extension = file_name.removeprefix('.')
    fn: Callable
    if extension == "txt":
        fn = TxtParser().parse
    elif extension == "pdf":
        fn = PdfParser().parse
    elif extension == "docx":
        fn = WordParser().parse
    elif extension == "pptx":
        fn = PptParser().parse
    elif extension == "xlsx":
        fn = ExcelParser().parse
    else:
        msg = f"The current given {extension= } doesn't have the neccesary parser implemented"
        logging.exception(msg)
        raise Exception(msg)
    return fn