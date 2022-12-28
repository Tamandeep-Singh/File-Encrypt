# -----------------------------------------------------------
# filename: encryptor.py
#
# Description: Provides a wrapper around the Fernet class so that data can easily be encrypted and decrypted
# Github Repo: https://github.com/Tamandeep-Singh/File-Encryptor
# Released under MIT License 
# -----------------------------------------------------------

from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key: bytes):
        """Constructor that initializes the fernet object with the key that is provided."""
        self.key = key
        self.fernet = Fernet(key)

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
