import logging
from pathlib import Path
import traceback
from typing import Union
from .parsers import get_parser

def _generate_parser_and_read(abs_file_path: str) -> Union[str, None]:
    ext = Path(abs_file_path).suffix
    try: 
        return get_parser(ext)(abs_file_path)
    except:
        traceback.print_exc()
        logging.exception(f"Parsing the file failded {abs_file_path= }")
        return None