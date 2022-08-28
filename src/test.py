import os
from PlagarismCecker import check_plagiarism_in_folder
abs_folder_path = os.path.abspath("./data")

cm = check_plagiarism_in_folder(abs_folder_path, ".txt")
cm = sorted(cm, key=lambda x: x[2], reverse=True)
print(cm)
