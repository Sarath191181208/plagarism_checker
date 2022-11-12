from pptx import Presentation 
import glob
from .base_class import BaseParser

class PptParser(BaseParser):
    @staticmethod
    def parse(abs_file_name: str) -> str:
        with open(abs_file_name, mode='rb') as f:
            for eachfile in glob.glob("*.pptx"):
               prs = Presentation(eachfile)
               print(eachfile)
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        print(shape.text)



    
