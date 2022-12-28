from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(key)

    def encrypt(self, data):
        return self.fernet.encrypt(data)

    def decrypt(self, encrypted_data):
        return self.fernet.decrypt(encrypted_data)

    @staticmethod
    def generate_random_key():
        return Fernet.generate_key()
