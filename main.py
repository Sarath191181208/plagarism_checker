from fileinput import filename
import traceback
import eel
from src.PlagarismCecker import check_plagiarism_in_folder

# name of folder where the html, css, js, image files are located
eel.init('templates')

@eel.expose
def uploadFolder(file_name: str, extension: str ):
    print(file_name, extension)
    try: 
        return list(check_plagiarism_in_folder(file_name, extension))
    except ValueError as e: # i.e empty folder (or) no files with the given extension
        traceback.print_exc()
        return None

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))