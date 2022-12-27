import os.path
from cryptography.fernet import Fernet


def log(message):
    LOG_TAG = "[FileEncryptor]"
    print(f"{LOG_TAG}: {message}\n")


def get_file_data(filename, mode):
    does_file_exist = os.path.exists(filename)
    if does_file_exist:
        with open(filename, mode) as file:
            return file.read()

    else:
        log(f"(get_file_data): File not found -> \"{filename}\" ")
        return


def get_crypto_key():
    key_filename = "../cryptography_key.txt"
    key = get_file_data(key_filename, 'rb')
    if key is None:
        log("(get_crypto_key): Unable to retrieve cryptography key from file. Created random key instead (please save).")
        key = Fernet.generate_key()
        log(f"(encrypt): Cryptography Key: {key}")
    return key

        
def init_fernet():
    key = get_crypto_key()
    return Fernet(key)

def encrypt(fernet, data):
    return fernet.encrypt(data)


def decrypt(fernet, encrypted_data):
    return fernet.decrypt(encrypted_data)


def process_file_data(filename):
    file_data = get_file_data(filename, 'rb')
    if file_data is None:
        return
    
    fernet = init_fernet()
    encrypted_file_data = encrypt(fernet, file_data)
    log(f"(process_file_data): Encrypted File Data -> Result: {encrypted_file_data}")
    



process_file_data("../test.txt")