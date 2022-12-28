import file_utils as FileUtils
import time
from encryptor import Encryptor
from logger import Logger


file_encryptor_logger = Logger("[FileEncryptor]")

def get_epoch_timestamp():
    return int(time.time())


def get_encryptor_instance():
    key_filename = "../cryptography_key.txt"
    key = FileUtils.get_file_data(key_filename, 'rb')
    if key is None:
        key = Encryptor.generate_random_key()
        file_encryptor_logger.log(f"<get_crypto_key>: Key file not found. Created Random Key: {key}")
        FileUtils.write_to_file("../cryptography_key.txt", key.decode('utf-8'), "w")
    
    return Encryptor(key)


def save_to_json_file(filename, data):
    original_file = FileUtils.get_file_without_ext(filename)
    encryption_filename = original_file + "_encrypted.json"
    data = { 
        'processed_file': filename,
        'data': data,
        'timestamp': get_epoch_timestamp()
    }
    FileUtils.write_to_file_json(encryption_filename, data, 'w')


        

def process_file_data(filename):
    file_data = FileUtils.get_file_data(filename, 'rb')
    if file_data is None:
        return
    
    fernet_encryptor = get_encryptor_instance()
    encrypted_file_data = fernet_encryptor.encrypt(file_data).decode('utf-8')
    file_encryptor_logger.log(f"<process_file_data>: Encrypted File Data -> Result: {encrypted_file_data}")
    save_to_json_file(filename, encrypted_file_data)

    



process_file_data("../test.txt")