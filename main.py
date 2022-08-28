import os
import tkinter
from tkinter import messagebox 
import tkinter.filedialog as filedialog
import traceback
import eel
from src.PlagarismCecker import check_plagiarism_in_folder

# name of folder where the html, css, js, image files are located
eel.init('templates')

@eel.expose
def selectFolder() -> str:
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    # directory_path  = filedialog.askdirectory();
    file_path = filedialog.askopenfilename(title="Choose a file to process whole folder")
    directory_path = os.path.dirname(file_path)
    return directory_path

def sort_mat(confusion_matrix: list[str, str, float]) -> list[str, str, list]:
    cm = sorted( confusion_matrix, key= lambda x : x[2], reverse=True)
    return cm  

@eel.expose
def uploadFolder(file_name: str):
    print(file_name)
    try: 
        data =  list(check_plagiarism_in_folder(file_name))
        data = sort_mat(data)
        return data
    except ValueError as e: # i.e empty folder (or) no files with the given extension
        traceback.print_exc()
        return None

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))