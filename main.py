from typing import Union
import os
import re
import tkinter
import tkinter.filedialog as filedialog
import traceback
from typing import List, Tuple
import eel
from src import check_plagiarism_in_folder

from src.parser_generator import _generate_parser_and_read
from src.parsers.HTML_parser import HTMLParser
from src.plagarism_checker import compare_files

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
        print(e)
        print(traceback.format_exc())
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
        print(e)
        print(traceback.format_exc())
    print(file_path)
    return file_path

def search_chunk_on_web(chunk: str) -> list[str, str, float]:
    from googlesearch import search

    query = str(chunk)
    url_list: list[str] = []
    for search_url in search(query, tld="co.in", num=2, stop=2, pause=0.1):
        url_list.append(search_url)
        text_list = [get_text_from_url(url) for url in url_list]

    # remove None from zipped list
    zipped = list(zip(url_list, text_list))
    zipped = [x for x in zipped if x[1] is not None]
    url_list, text_list = zip(*zipped)


    res_list = compare_files([*text_list, query], [*url_list, "query"])
    res_list = [res for res in res_list if res[0] == "query" or res[1] == "query"]
    res_list = sort_mat(res_list)

    res = res_list[0]
    res_1 = res[1] if res[1] != "query" else res[0]

    return (query , res_1, res[2])

def get_text_from_url(url: str) -> Union[str, None]:
    import requests
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return HTMLParser.parse_html(  r.text )
    except requests.exceptions.RequestException as err:
        print ("Oops: Something Else",err)
        return None

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
    try: 
        data =  list(check_plagiarism_in_folder(folder_path))
        data = sort_mat(data)
        return data
    except ValueError as e: # i.e empty folder (or) no files with the given extension
        print(e)
        traceback.print_exc()
        return None
    except Exception as e:
        traceback.print_exc()
        print("Some exception occured")
        return None

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))