import pandas as pd
from .base_class import BaseParser

class ExcelParser(BaseParser):
    @staticmethod
    def parse(abs_file_name: str) -> str:
        with open(abs_file_name, mode='rb') as f:
           excelreader=pd.read_excel(f)
        return(excelreader)




           