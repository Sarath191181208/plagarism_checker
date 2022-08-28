from fileinput import filename
import traceback
import eel
from src.PlagarismCecker import check_plagiarism_in_folder

# name of folder where the html, css, js, image files are located
eel.init('templates')

def sort_mat(confusion_matrix: list[str, str, float]) -> list[str, str, list]:
    cm = sorted( confusion_matrix, key= lambda x : x[2], reverse=True)
    return cm  

@eel.expose
def uploadFolder(file_name: str, extension: str ):
    print(file_name, extension)
    try: 
        return sort_mat(list(check_plagiarism_in_folder(file_name, extension)))
    except ValueError as e: # i.e empty folder (or) no files with the given extension
        traceback.print_exc()
        return None

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))