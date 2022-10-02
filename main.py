import logging
import os
import tkinter
import tkinter.filedialog as filedialog
import traceback
import eel
from src import check_plagiarism_in_folder

import logging
logging.basicConfig(filename='logs.log', 
    level=logging.DEBUG, 
    format='%(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p')

eel.init('templates')

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
    except:
        pass
    print(directory_path)
    return directory_path

def sort_mat(confusion_matrix: list[str, str, float]) -> list[str, str, list]:
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