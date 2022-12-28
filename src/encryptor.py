from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key: bytes):
        self.key = key
        self.fernet = Fernet(key)

    def encrypt(self, data:bytes) -> bytes:
        return self.fernet.encrypt(data)

    def decrypt(self, encrypted_data:bytes) -> bytes:
        return self.fernet.decrypt(encrypted_data)

    @staticmethod
    def generate_random_key() -> bytes:
        return Fernet.generate_key()
