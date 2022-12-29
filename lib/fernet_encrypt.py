# -----------------------------------------------------------
# filename: fernet_encrypt.py
#
# Description: Provides a wrapper around the Fernet class so that data can easily be encrypted and decrypted
# Github Repo: https://github.com/Tamandeep-Singh/File-Encrypt
# Released under MIT License 
# -----------------------------------------------------------

from cryptography.fernet import Fernet
from logger import Logger
import file_utils as FileUtils

encryptor_logger = Logger("[FernetEncrypt]")

class FernetEncrypt:
    def __init__(self):
        """Constructor that initializes the fernet object with the key that is provided."""
        self.key = FernetEncrypt.get_encryptor_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, data:bytes) -> bytes:
        """Returns the encrypted bytes of the data parameter."""
        return self.fernet.encrypt(data)

    def decrypt(self, encrypted_data:bytes) -> bytes:
        """Returns the decrypted bytes of the encrypted_data parameter."""
        return self.fernet.decrypt(encrypted_data)

    @staticmethod
    def generate_random_key() -> bytes:
        """Static method that returns a randomized url-safe 32 character base64 encoded key in bytes."""
        return Fernet.generate_key()

    @staticmethod
    def get_string(data: bytes) -> str:
        """Returns the data parameter (in bytes) to its equivalent string representation."""
        return data.decode('utf-8')

    @staticmethod
    def get_bytes(data: str) -> bytes:
        """Returns the data parameter (as a string) to its equivalent bytes representation."""
        return data.encode('utf-8')

    @staticmethod
    def get_encryptor_key() -> bytes:
        """Returns the encryption key from the key file or if not found, generates a random key and saves it to the key file."""
        key_filename = "../cryptography_key.txt"
        key = FileUtils.get_file_data(key_filename, 'rb')
        if key is None:
            key = FernetEncrypt.generate_random_key()
            encryptor_logger.log(f"<get_encryptor_key>: Key file not found. Created Random Key: {key}")
            FileUtils.write_to_file("../cryptography_key.txt", key.decode('utf-8'), "w")
        return key
    

    
