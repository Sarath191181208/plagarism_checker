import eel
from src.PlagarismCecker import check_plagiarism_in_folder

# name of folder where the html, css, js, image files are located
eel.init('templates')

@eel.expose
def demo(file_name: str, extension: str ):
    try: 
        return check_plagiarism_in_folder(file_name, extension)
    except ValueError: # i.e empty folder (or) no files with the given extension
        return None
# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))