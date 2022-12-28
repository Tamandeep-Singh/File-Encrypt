import os
import json
from logger import Logger


file_utils_logger = Logger("[FileUtils]")

def does_file_exist(filename:str) -> bool:
    return os.path.exists(filename)
    
    
def get_file_data(filename:str, mode:str) -> str | None:
    file_exists = does_file_exist(filename)
    if file_exists:
        with open(filename, mode) as file:
            return file.read()
            
    file_utils_logger.log(f"<get_file_data>: File not found -> \"{filename}\" ")
    return None


def get_file_without_ext(filename:str) -> str:
    return os.path.splitext(filename)[0]

def write_to_file(filename:str, data:str, mode:str) -> None:
    file = open(filename, mode)
    file.write(data)
    file.close()
    file_utils_logger.log(f"<write_to_file: wrote file data to {filename}")


def write_to_file_json(filename:str, data:str, mode:str) -> None:
    file = open(filename, mode)
    data = json.dumps(data)
    file.write(data)
    file.close()
    file_utils_logger.log(f"<write_to_file_json: wrote file data to {filename}")

    


    
        