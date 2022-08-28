import os
from PlagarismCecker import check_plagiarism_in_folder
abs_folder_path = os.path.abspath("./data")

print(check_plagiarism_in_folder(abs_folder_path, ".txt"))
