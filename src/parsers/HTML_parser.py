from bs4 import BeautifulSoup
from .base_class import BaseParser
class WordParser(BaseParser):
    @staticmethod
    def parse(abs_file_name: str) -> str:
        with open(abs_file_name, mode='rb') as f:
            return WordParser.parse_html(BeautifulSoup(f, 'html.parser'))

    @staticmethod
    def parse_html(html_content: str)  -> str:
        soup = BeautifulSoup(html_content, features="html.parser")

        # remove all javascript and stylesheet code
        for script in soup(["script", "style"]): script.extract()  

        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return(text)
