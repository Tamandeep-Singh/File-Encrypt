# -----------------------------------------------------------
# filename: file_encryptor.py
#
# Description: Main python script that is used to encrypt a file's contents and save the encrypted data into a corresponding JSON file
# Github Repo: https://github.com/Tamandeep-Singh/File-Encryptor
# Released under MIT License 
# -----------------------------------------------------------

import file_utils as FileUtils
import time
from encryptor import Encryptor
from logger import Logger


file_encryptor_logger = Logger("[FileEncryptor]")

def get_epoch_timestamp() -> int:
    """Returns the current Unix Epoch Timestamp."""
    return int(time.time())


def get_filename() -> str:
    """Gets the filename that the user wants to encrypt."""
    return input("Enter the filename for the file you want to encrypt: ")

def get_encryptor_instance() -> Encryptor:
    """Creates and returns a new Encryptor instance with the key either being already provided or randomly generated."""
    key_filename = "../cryptography_key.txt"
    key = FileUtils.get_file_data(key_filename, 'rb')
    if key is None:
        key = Encryptor.generate_random_key()
        file_encryptor_logger.log(f"<get_crypto_key>: Key file not found. Created Random Key: {key}")
        FileUtils.write_to_file("../cryptography_key.txt", key.decode('utf-8'), "w")
    
    return Encryptor(key)


def save_to_json_file(filename:str, data:str) -> None:
    """Saves the encrypted file data to a JSON file with metadata detailing the timestamp and original file processed."""
    original_file = FileUtils.get_file_without_ext(filename)
    encryption_filename = original_file + "_encrypted.json"
    data = { 
        'processed_file': filename,
        'data': data,
        'timestamp': get_epoch_timestamp()
    }
    FileUtils.write_to_file_json(encryption_filename, data, 'w')


        

def process_file_data(filename:str) -> None:
    """Processes the file chosen by the user and produces the encrypted output into a JSON file"""
    file_data = FileUtils.get_file_data(filename, 'rb')
    if file_data is None:
        return
    
    fernet_encryptor = get_encryptor_instance()
    encrypted_file_data = fernet_encryptor.encrypt(file_data).decode('utf-8')
    file_encryptor_logger.log(f"<process_file_data>: Encrypted File Data -> Result: {encrypted_file_data}")
    save_to_json_file(filename, encrypted_file_data)

    

def main() -> None:
    """Main method that controls the execution of getting the filename from the user and encrypting the file."""
    filename = get_filename()
    process_file_data(filename)


if __name__ == "__main__":
    main()
