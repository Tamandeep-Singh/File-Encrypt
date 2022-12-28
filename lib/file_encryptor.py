# -----------------------------------------------------------
# filename: file_encryptor.py
#
# Description: Main python script that is used to encrypt a file's contents and save the encrypted data into a corresponding JSON file
# Github Repo: https://github.com/Tamandeep-Singh/File-Encryptor
# Released under MIT License 
# -----------------------------------------------------------

import file_utils as FileUtils
import json
import time
from encryptor import Encryptor
from logger import Logger


file_encryptor_logger = Logger("[FileEncryptor]")
fernet_encryptor = Encryptor()

def get_epoch_timestamp() -> int:
    """Returns the current Unix Epoch Timestamp."""
    return int(time.time())


def get_user_option() -> int:
    """Loops the menu until a valid option is entered and returned."""
    option = -1
    print("File Encryption: Menu")
    print("1. Encrypt File")
    print("2. Decrypt File")
    while option != 1 and option != 2:
        option = int(input ("Enter your option: "))

    return option
        


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


def process_file_data(filename: str = None) -> None:
    """Processes the file chosen by the user and produces the encrypted output into a JSON file"""
    if filename is None:
        filename = input("Enter the filename for the file you want to encrypt: ")

    file_data = FileUtils.get_file_data(filename, 'rb')

    if file_data is None:
        return

    encrypted_file_data = fernet_encryptor.encrypt(file_data).decode('utf-8')
    file_encryptor_logger.log(f"<process_file_data>: Encrypted File Data -> Result: {encrypted_file_data}")
    save_to_json_file(filename, encrypted_file_data)


def decrypt_json_file(json_filename:str = None) -> None:
    """Decrypts an encrypted JSON file and prints the decrypted data."""

    if json_filename is None:
        json_filename = input("Enter the encrypted JSON filename: ")
        
    json_data = json.loads(FileUtils.get_file_data(json_filename, 'r'))
    if json_data is None:
        return
    encrypted_data = json_data['data'].encode('utf-8')
    decrypted_data = fernet_encryptor.decrypt(encrypted_data).decode('utf-8')
    file_encryptor_logger.log(f"<decrypt_json_file>: Decrypted data: {decrypted_data}")

    

def main() -> None:
    """Main method that controls the execution of getting the filename from the user and encrypting the file."""
    option = get_user_option()
    if option == 1:
        process_file_data()
    elif option == 2:
        decrypt_json_file()
    

if __name__ == "__main__":
    main()
