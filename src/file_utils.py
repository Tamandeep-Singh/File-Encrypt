import os
from logger import Logger

file_utils_logger = Logger("[FileUtils]")

def does_file_exist(filename):
    return os.path.exists(filename)
    
    
def get_file_data(filename, mode):
    file_exists = does_file_exist(filename)
    if file_exists:
        with open(filename, mode) as file:
            return file.read()
            
    file_utils_logger.log(f"<get_file_data>: File not found -> \"{filename}\" ")
    return None