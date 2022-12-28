import file_utils as FileUtils
from encryptor import Encryptor
from logger import Logger


file_encryptor_logger = Logger("[FileEncryptor]")


def get_encryptor_instance():
    key_filename = "../cryptography_key.txt"
    key = FileUtils.get_file_data(key_filename, 'rb')
    if key is None:
        key = Encryptor.generate_random_key()
        file_encryptor_logger.log(f"<get_crypto_key>: Key file not found. Created Random Key: {key}")
    
    return Encryptor(key)

        

def process_file_data(filename):
    file_data = FileUtils.get_file_data(filename, 'rb')
    if file_data is None:
        return
    
    fernet_encryptor = get_encryptor_instance()
    encrypted_file_data = fernet_encryptor.encrypt(file_data)
    file_encryptor_logger.log(f"<process_file_data>: Encrypted File Data -> Result: {encrypted_file_data}")
    



process_file_data("../test.txt")