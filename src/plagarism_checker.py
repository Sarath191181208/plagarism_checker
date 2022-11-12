import os
import traceback
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Tuple, Union

from src.parser_generator import _generate_parser_and_read

from .parsers import get_parser

import logging

def vectorize(txt: str)-> np.ndarray: return TfidfVectorizer().fit_transform(txt).toarray() # text to vectors
def similarity(doc1: str, doc2: str) -> float: return cosine_similarity([doc1, doc2]) # similarity between files range(0-1)

def check_plagiarism_in_folder(abs_folder_path: str) -> list[str, str, float]:

    user_files = [doc for doc in os.listdir(abs_folder_path) if not os.path.isdir(doc)]      # getting all the files 
    
    logging.debug(f"{user_files= }")
    logging.debug([os.path.join(abs_folder_path, file_name) for file_name in user_files])

    user_notes = {file_name : _generate_parser_and_read(os.path.join(abs_folder_path, file_name).replace("\\", "/")) 
                for file_name in user_files} # parsing all the files
    user_notes = {k:v for k,v in user_notes.items() if v} # i.e v is truthy (not (None or empty))
    user_files, user_notes = zip(*user_notes.items())

    logging.debug(f"{abs_folder_path= }")
    logging.debug(f"turnicated user_notes = {[note[:20] for note in user_notes]}")

    return compare_files(user_notes, user_files)

def compare_files(user_notes: list[str], user_files: list[str]) -> list[Tuple[str, str, float]]:
    """
        compares the different files and scores the results 
        Prameters:
        ---
        user_notes: list[str] -> [note1, note2, note3, ...]
        user_files: list[str] -> [file_name, file_name, ...]

        Returns:
        ---
        [
            (file_name1, file_name2, score),
            (file_name1, file_name3, score),
        ]

        returns a list of tuples (file1, file2, similarity_score)
    """
    txt_vectors = vectorize(user_notes) # list[str] -> vectors
    s_vectors = list(zip(user_files, txt_vectors)) # merging filenames and vectors
    plagiarism_results = set()

    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1], int(sim_score*100))
            plagiarism_results.add(score)

    return sorted(plagiarism_results, key= lambda x : x[2], reverse=True)  # sort results on score  
if __name__ == "__main__":
    abs_folder_path = "E:\Sarath\python\Plagarism_cheker\data/pdf"
    # try: 
    for data in check_plagiarism_in_folder(abs_folder_path):
        print("data", data)
    # except ValueError: # i.e empty folder (or) no files with the given extension
    #     print("Here ... ")