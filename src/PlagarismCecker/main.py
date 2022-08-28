import os
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import  Callable
import textract


textract_supported_files = [
"csv" ,"doc" ,"docx","eml" ,"epub" ,
"gif" ,"jpg" ,"json","html","mp3"  ,"msg" ,
"odt" ,"ogg" ,"pdf" ,"png" ,"pptx" ,"ps" ,
"rtf" ,"tiff","txt" ,"wav" ,"xlsx" ,"xls" ,
]

def get_file_parser(extension: str) -> Callable[ str, str]:
    """returns a function to read a file the function takes the absolute path of a file and returns text"""
    extension = extension.removeprefix('.')
    fn: callable
    if extension in textract_supported_files:
        fn = textract.process
    else:
        raise Exception("The current given extension doesn't have the neccesary parser implemented")
    return fn

def vectorize(txt: str)-> np.ndarray: return TfidfVectorizer().fit_transform(txt).toarray() # text to vectors
def similarity(doc1: str, doc2: str) -> float: return cosine_similarity([doc1, doc2]) # similarity between files range(0-1)

def check_plagiarism_in_folder(abs_folder_path: str, extension: str) -> list[str, str, float]:

    user_files = [doc for doc in os.listdir(abs_folder_path) 
                if doc.endswith(extension)]      # getting all the files 
    file_parser = get_file_parser(extension)     # creating a parser
    user_notes = [file_parser(os.path.join(abs_folder_path, abs_file_name)) 
                for abs_file_name in user_files] # parsing all the files


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
            score = (student_pair[0], student_pair[1], sim_score)
            plagiarism_results.add(score)

    return plagiarism_results

if __name__ == "__main__":
    abs_folder_path = "E:\Sarath\python\Plagarism_cheker\data"
    e = '.txt'
    try: 
        for data in check_plagiarism_in_folder(abs_folder_path, e):
            print(data)
    except ValueError: # i.e empty folder (or) no files with the given extension
        print("Here ... ")