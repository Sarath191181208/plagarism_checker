from ctypes import Union
import logging
import os
import re
import tkinter
import tkinter.filedialog as filedialog
import traceback
from typing import List, Tuple
import eel
from src import check_plagiarism_in_folder

import logging

from src.parser_generator import _generate_parser_and_read

logging.basicConfig(filename='logs.log', 
    level=logging.DEBUG, 
    format='%(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p')

eel.init('templates', js_result_timeout=5*60*60)

@eel.expose
def selectFolder() -> str:
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    directory_path = None
    # directory_path  = filedialog.askdirectory();
    try: 
        file_path = filedialog.askopenfilename(title="Choose a file to process whole folder")
        directory_path = os.path.dirname(file_path)
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
    print(directory_path)
    return directory_path

@eel.expose
def selectFile() -> str:
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    file_path = None
    try:
        file_path = filedialog.askopenfilename(title="Choose a file to process")
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
    print(file_path)
    return file_path

def search_chunk_on_web(chunk: str) -> list[str, str, float]:
    from googlesearch import search

    # to search
    query = str(chunk)
    for search_url in search(query, tld="co.in", num=2, stop=1, pause=0.2):
        # TODO: get the similarity score from the search result and take the max score
        print(search_url)
    return [chunk, search_url, 0.0]


@eel.expose
def parseFileAndSearch(file_path: str) -> List[Tuple[str, str, float]]:
    text: Union[str, None] =  _generate_parser_and_read(file_path)
    if text is None: return None
    text_chunks: List[str] = re.split(r'[\s.,;:!? ]+', text)
    text_chunks = [" ".join(text_chunks[i:i+32]) for i in range(0, len(text_chunks), 32)]
    res_obj = [search_chunk_on_web(chunk) for chunk in text_chunks]
    return res_obj

def sort_mat(confusion_matrix: list[str, str, float]) -> list[str, str, float]:
    _cm = sorted( confusion_matrix, key= lambda x : x[2], reverse=True)
    return _cm  

@eel.expose
def uploadFolder(folder_path: str):
    logging.info("folder_path: ",folder_path)
    try: 
        data =  list(check_plagiarism_in_folder(folder_path))
        data = sort_mat(data)
        return data
    except ValueError as e: # i.e empty folder (or) no files with the given extension
        traceback.print_exc()
        logging.exception("Empty folder")
        return None
    except Exception as e:
        traceback.print_exc()
        logging.exception("Some exception occured")
        return None

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))